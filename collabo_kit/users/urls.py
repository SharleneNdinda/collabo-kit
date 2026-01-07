"""Auth URLs."""

from django.urls import path

from .views import (CustomTokenObtainPairView, CustomTokenRefreshView,
                    RegistrationView)

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegistrationView.as_view(), name="register"),
]
