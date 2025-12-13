"""Auth URLs."""

from django.urls import path

from collabo_kit.users.views import LoginView, RegistrationView


urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
