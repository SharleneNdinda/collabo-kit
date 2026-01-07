from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CollaboUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Override the default SimpleJWT `TokenObtainPairSerializer` to add custom fields."""

    @classmethod
    def get_token(cls, user: CollaboUser) -> dict[str, str]:
        """Add custom fields to the token."""
        token = super().get_token(user)
        token["email"] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=False,
        style={"input_type": "password"},
    )

    """
    Collabo User Serializer.
    """

    class Meta:
        """Serializer options."""

        model = CollaboUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "is_staff",
            "is_active",
            "created",
            "updated",
        )

    def create(self, validated_data):
        return CollaboUser.objects.create_user(**validated_data)
