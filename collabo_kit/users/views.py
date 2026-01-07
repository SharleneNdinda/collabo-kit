from rest_framework import generics, permissions
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from collabo_kit.users.serializers import (CustomTokenObtainPairSerializer,
                                           UserSerializer)


class CustomTokenObtainPairView(TokenObtainPairView):
    """View that returns a JWT token."""

    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    """View that refreshes a JWT token."""

    serializer_class = TokenRefreshSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
