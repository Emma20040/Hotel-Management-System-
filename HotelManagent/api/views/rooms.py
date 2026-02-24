from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from api.serializers.rooms import RoomTypeSerializer
from booking.models import RoomType


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAdminUser])
def create_roomType(request):
    serializer =RoomTypeSerializer(data =request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Roomtype created sucessfully!!!",
                "roomType": serializer.data
            },
            status = status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([AllowAny])
def get_roomType(request):
    roomType = RoomType.objects.first()
    serializer = RoomTypeSerializer(roomType)
    return Response(serializer.data)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([AllowAny])
# def hotel_details(request):
#     hotel = Hotel.objects.first()
#     if not hotel:
#         return Response(
#             {"error": "No hotel found. "},
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     serializer = HotelSerializer(hotel)
#     return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def update_roomType(request):
    roomType = RoomType.objects.first()
    serializer = RoomTypeSerializer(roomType, data= request.data, partial- True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['PUT'])
# @authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAdminUser])
# def update_hotel(request):
#     hotel = Hotel.objects.first()
#     if not hotel:
#         return Response(
#             {'error': 'hotel not found'},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     serializer = HotelSerializer(hotel, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {'message': 'hotel updated successfully',
#              'hotel': serializer.data}
#         )
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def delete_roomType(request):
    roomType = RoomType.objects.first()
    rommType.delete()

# @api_view(['DELETE'])
# @authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAdminUser])
# def delete_hotel(request):
#     hotel = Hotel.objects.first()
#     if not hotel:
#         return Response(
#             {'error': 'hotel not found'},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     hotel.delete()
#     return Response(
#         {'message': 'hotel deleted successfully'},
#         status=status.HTTP_200_OK
#     )