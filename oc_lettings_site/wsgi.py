"""
WSGI configuration for the oc_lettings_site project.

This module exposes the WSGI callable as a module-level variable
named `application`. It serves as the entry point for
WSGI-compatible web servers to serve your Django project.

The WSGI configuration loads the project's settings module and
prepares the Django application for handling requests.

Functions:
    get_wsgi_application:
        Returns a WSGI callable to handle requests.

Environment Variables:
    DJANGO_SETTINGS_MODULE (str):
        The Python path to the settings module for this Django project.

Example:
    To run the application with a WSGI server such as Gunicorn:

        $ gunicorn oc_lettings_site.wsgi:application
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'oc_lettings_site.settings'
)

application = get_wsgi_application()
