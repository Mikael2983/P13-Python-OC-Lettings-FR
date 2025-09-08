"""
Application configuration for the profiles app.

This module defines the configuration class for the profiles application,
used by Django to set up application-specific settings.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
        Configuration class for the profiles application.

        Attributes:
            name (str): The full Python path to the application.
        """
    name = 'profiles'
