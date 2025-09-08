import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_profile_detail_view(client, profile):
    """
    Integration test:
    - Access the detail page of a profile
    - Check that the username is displayed
    """
    url = reverse("profile", args=[profile.user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert profile.user.first_name in response.content.decode()
    assert profile.favorite_city in response.content.decode()


@pytest.mark.django_db
def test_profiles_index_view(client, profile):
    """
    Integration test:
    - Access the index page of the lettering
    - Check that the username of the user is listed
    """
    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert profile.user.username in response.content.decode()


@pytest.mark.django_db
def test_profile_str_method(profile):
    """Test the string representation of Profile."""
    assert str(profile) == profile.user.username
