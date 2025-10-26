from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Users.apps import UsersConfig
from Users.views import UserCreateAPIView


app_name = UsersConfig.name

urlspatterns = [
    path("obtain/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("register_user/", UserCreateAPIView.as_view(), name="register"),
]