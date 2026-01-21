from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token

from api.serializers.authentication import UserSerializer, RegisterUserSerializer, LoginSerializer
from Authentication.models import CustomUser

# Home
@api_view(['GET'])
@permission_classes([AllowAny])
def api_home(request):
    return Response({
        'message': 'Hotel Management API',
        'endpoints': {
            'register': 'POST /api/auth/register/',
            'login': 'POST /api/auth/login/',
            'logout': 'POST /api/auth/logout/',
            'profile': 'GET /api/auth/profile/',
        }
    })

# Register
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        
        return Response({
            'message': 'User created',
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        from django.contrib.auth import authenticate
        user = authenticate(request, email=email, password=password)
        
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'message': 'Login successful',
                'user': UserSerializer(user).data,
                'token': token.key
            })
    
    return Response(
        {'error': 'Invalid credentials'}, 
        status=status.HTTP_400_BAD_REQUEST
    )

# Logout
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out'})

# Profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# Get Token
@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    from django.contrib.auth import authenticate
    from rest_framework.authtoken.views import ObtainAuthToken
    
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, email=email, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
    return Response(
        {'error': 'Invalid credentials'}, 
        status=status.HTTP_400_BAD_REQUEST
    )

# List Users (Admin only)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def users_list(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)