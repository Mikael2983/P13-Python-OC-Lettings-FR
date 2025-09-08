"""
Models for managing user profiles.

This module defines the database schema for storing additional
information related to users in the application.

Classes:
    Profile:
        Represents a user profile extending Django's built-in User model
        with additional information, such as the user's favorite city.

The models use Django's ORM for database interaction and include
validation rules for field values.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (OneToOneField):
            A one-to-one relationship to Django's built-in User model.
            Deleting the user will also delete the profile.
        favorite_city (CharField):
            The user's preferred city, up to 64 characters.

    Methods:
        __str__:
            Returns the username of the associated user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a human-readable string representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
