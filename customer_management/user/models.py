from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import EmailValidator


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True, 
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Fix conflicts by adding unique related_name
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    USERNAME_FIELD = 'email'  # Use email instead of username for authentication
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email