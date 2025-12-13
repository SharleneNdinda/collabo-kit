import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CollaboUser(AbstractUser):
    id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["first_name", "last_name, email"]

    class Meta:
        """Model options."""

        ordering = (
            "-updated",
            "-created",
        )
