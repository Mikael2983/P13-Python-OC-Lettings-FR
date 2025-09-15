import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_list_view(client, profile):
    """
    Test that the profiles list page renders correctly and shows the username.
    """
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200
    assert profile.user.username in response.content.decode()


@pytest.mark.django_db
def test_profile_detail_view(client, profile):
    """
    Test that the profile detail page renders correctly and shows the favorite city.
    """
    url = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert profile.user.username in content
    assert profile.favorite_city in content


@pytest.mark.django_db
def test_profile_404(client):
    """
    Accessing a non-existent profile should return a 404 page.
    """
    url = reverse('profile', kwargs={'username': "unknow"})
    response = client.get(url)
    assert response.status_code == 404
    assert "Page not found" in response.content.decode()
