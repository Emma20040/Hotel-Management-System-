from django.urls import path
from Authentication.views import signup, login_user, logout_user
from rest_framework.authtoken.views import obtain_auth_token
from api.views import authentication

urlpatterns = [
    # Home
    path('', authentication.api_home, name='api-home'),
    
    # Auth
    path('auth/register/', authentication.register, name='api-register'),
    path('auth/login/', authentication.login_view, name='api-login'),
    path('auth/logout/', authentication.logout_view, name='api-logout'),
    path('auth/profile/', authentication.profile, name='api-profile'),
    path('auth/users/', authentication.users_list, name='api-users-list'),
    
    # Token
    path('auth/token/', obtain_auth_token, name='api-token'),
    path('auth/get-token/', authentication.get_token, name='api-get-token'),
]