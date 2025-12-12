"""Auth URLs."""

from django.urls import path

from collabo_kit.users.views import LoginView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
