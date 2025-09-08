"""
Views for the lettings application.

This module contains view functions for displaying the list of lettings
and the details of a specific letting.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the list of all lettings.

    Retrieves all `Letting` instances from the database and passes them
    to the `lettings/index.html` template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page showing all lettings.

    Template context:
        lettings_list (QuerySet): A queryset containing all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Display the details of a single letting.

    Retrieves the `Letting` instance matching the given ID and passes
    its details to the `lettings/letting.html` template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The primary key of the letting to display.

    Returns:
        HttpResponse: The rendered HTML page showing the letting details.

    Template context:
        title (str): The title of the letting.
        address (Address): The address object related to the letting.

    Raises:
        Http404: If no letting exists with the given `letting_id`.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
