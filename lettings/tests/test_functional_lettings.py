import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_list_view(client, letting):
    """
    Test that the lettings list page renders correctly and contains the letting title.
    """
    url = reverse('lettings_index')
    response = client.get(url)
    assert response.status_code == 200
    assert letting.title in response.content.decode()


@pytest.mark.django_db
def test_letting_detail_view(client, letting):
    """
    Test that the letting detail page renders correctly and shows the address.
    """
    url = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert letting.title in content
    assert letting.address.street in content
    assert letting.address.city in content


@pytest.mark.django_db
def test_letting_404(client):
    """
    Accessing a non-existent letting should return a 404 page.
    """
    url = reverse('letting', kwargs={'letting_id': 9999})
    response = client.get(url)
    assert response.status_code == 404
    assert "Page not found" in response.content.decode()
