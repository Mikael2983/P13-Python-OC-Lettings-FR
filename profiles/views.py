"""
Views for the profiles application.

This module contains view functions for displaying the list of profiles
and the details of a specific profile.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request: HttpRequest) -> HttpResponse:
    """
        Display the list of all profiles.

        Retrieves all `Profile` instances from the database and passes them
        to the `profiles/index.html` template for rendering.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page showing all profiles.

        Template context:
            profiles_list (QuerySet): A queryset containing all profiles.
        """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
        Display the details of a single profile.

        Retrieves the `Profile` instance matching the given ID and passes
        its details to the `profiles/profile.html` template for rendering.

        Args:
            request (HttpRequest): The HTTP request object.
            username (string): The username of the profile to display.

        Returns:
            HttpResponse: The rendered HTML page showing the profile details.

        Template context:
            title (str): The title of the profile.
            address (Address): The address object related to the profile.

        Raises:
            Http404: If no profile exists with the given `profile_id`.
        """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
