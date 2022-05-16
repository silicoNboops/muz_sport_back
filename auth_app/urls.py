from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('user/', PersonalRoomViewSet.as_view({'get': 'retrieve'})),
]
