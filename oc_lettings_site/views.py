"""
Views for the main oc_lettings_site project.

This module contains views for the home page and custom error pages
(404 and 500).
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the home page of the project.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'index.html' template.
    """
    return render(request, 'index.html')


def custom_error_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """
    Handle 404 Page Not Found errors.

    This view is used automatically by Django when a requested page
    does not exist.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404.

    Returns:
        HttpResponse: The rendered 'errors/404.html' template with HTTP status code 404.
"""
    return render(request, "errors/404.html", status=404)


def custom_error_500(request: HttpRequest) -> HttpResponse:
    """
    Handle 500 Internal Server Error responses.

    This view is used automatically by Django when an unhandled server
    error occurs.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'errors/500.html' template with HTTP status code 500.
    """
    return render(request, "errors/500.html", status=500)
