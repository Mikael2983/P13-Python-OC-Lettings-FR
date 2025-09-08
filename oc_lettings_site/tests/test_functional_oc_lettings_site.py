import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """
    Test that the index page renders correctly.
    """
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()
