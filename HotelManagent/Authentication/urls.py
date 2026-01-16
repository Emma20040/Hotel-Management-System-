from django.urls import path
from Authentication import views
urlpatterns = [
    path('home/', views.home, name ='home'),
    path("signup/", views.signup, name="signup"),
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.login_user, name='logout-user')
    
]
