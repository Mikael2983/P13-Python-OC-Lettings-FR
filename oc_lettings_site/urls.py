"""
URL configuration for the oc_lettings_site project.

This module defines the URL routes for the entire project, including:
- The home page
- Django admin site
- Lettings app
- Profiles app
- Custom error handlers for 404 and 500 HTTP errors
"""
from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    """
    Intentionally triggers a server error (HTTP 500) for testing purposes.

    This view function divides 1 by 0 to raise a ZeroDivisionError,
    which allows developers to verify error monitoring, logging, or
    external error tracking tools (e.g., Sentry) are working correctly.

    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        int: This function does not return a valid response since it
        always raises an exception.

    Raises:
        ZeroDivisionError: Always raised due to division by zero.
    """
    division_by_zero = 1 / 0
    return division_by_zero

# -------------------------------------------------------------------
# Custom error handlers
# -------------------------------------------------------------------
# These handlers are automatically used by Django when a 404 or 500 error occurs


handler404 = "oc_lettings_site.views.custom_error_404"
handler500 = "oc_lettings_site.views.custom_error_500"

# -------------------------------------------------------------------
# URL patterns
# -------------------------------------------------------------------

urlpatterns = [
    path('test/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
