import uuid
from typing import Any, Optional, cast

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CollaboUserManager(BaseUserManager):
    """Django user manager for CollaboUser."""

    def create_user(
        self, email: str, password: Optional[str] = None, **fields: Any
    ) -> "CollaboUser":
        """Create a user."""
        user = cast(
            "CollaboUser", self.model(email=self.normalize_email(email), **fields)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **fields: Any) -> "CollaboUser":
        """Create a Django admin superuser."""
        user = self.create_user(**fields)
        user.is_staff = True
        user.save(using=self._db)
        return user


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

    objects = CollaboUserManager()

    REQUIRED_FIELDS = ["first_name", "last_name, email"]

    def __str__(self):
        return self.email

    class Meta:
        """Model options."""

        ordering = (
            "-updated",
            "-created",
        )
