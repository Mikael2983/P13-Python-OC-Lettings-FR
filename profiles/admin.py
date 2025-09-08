"""
Admin configuration for the profiles application.

This module registers the `Profile` model with the Django admin
site so they can be managed through the admin interface.
"""
from django.contrib import admin
from profiles.models import Profile


admin.site.register(Profile)
