from rest_framework import serializers

from .models import CollaboUser


class UserSerializer(serializers.ModelSerializer):
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
            "email",
            "is_staff",
            "is_active",
            "created",
            "updated",
        )
