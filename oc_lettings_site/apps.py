"""
App configuration for the oc_lettings_site project.

This module defines the configuration class for the
`oc_lettings_site` project. It specifies metadata and
settings used by Django to initialize the project.

Classes:
    OCLettingsSiteConfig(AppConfig):
        Configuration class for the oc_lettings_site project.

        Attributes:
            name (str): The full Python path to the project.
"""
from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """Configuration class for the oc_lettings_site project."""
    name = 'oc_lettings_site'
