"""
Admin configuration for the lettings application.

This module registers the `Letting` and `Address` models with the Django admin
site so they can be managed through the admin interface.
"""

from django.contrib import admin

from lettings.models import Letting
from .models import Address


admin.site.register(Letting)
admin.site.register(Address)
