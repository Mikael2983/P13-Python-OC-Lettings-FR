"""
URL configuration for the lettings application.

This module defines the URL patterns for the lettings app, mapping each
URL path to the appropriate view function.

Routes:
    '' (root of lettings app):
        Displays the list of all lettings.
    '<int:letting_id>/':
        Displays details for a specific letting identified by its ID.
"""
from django.urls import path

from . import views


# List of URL patterns for the lettings app
urlpatterns = [
    path('', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
