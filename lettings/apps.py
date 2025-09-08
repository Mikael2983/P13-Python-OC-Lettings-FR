"""
Application configuration for the lettings app.

This module defines the configuration class for the lettings application,
used by Django to set up application-specific settings.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings application.

    Attributes:
        name (str): The full Python path to the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
