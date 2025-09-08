"""
URL configuration for the profiles application.

This module defines the URL patterns for the profiles app, mapping each
URL path to the appropriate view function.

Routes:
    '' (root of profiles app):
        Displays the list of all profiles.
    '<int:profile_id>/':
        Displays details for a specific profile identified by its ID.
"""
from django.urls import path

from . import views


# List of URL patterns for the profiles app
urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
