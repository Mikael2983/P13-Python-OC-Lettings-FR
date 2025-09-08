import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_detail_view(client, letting):
    """
    Integration test:
    - Access the detail page of a Letting
    - Check that the address and title information are displayed
    """
    url = reverse("letting", args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert letting.title in response.content.decode()
    assert str(letting.address) in response.content.decode()


@pytest.mark.django_db
def test_lettings_index_view(client, letting):
    """
    Integration test:
    - Access the index page of the lettering
    - Check that the title of the lease is listed
    """
    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert letting.title in response.content.decode()


@pytest.mark.django_db
def test_create_letting_and_address_flow(client):
    """
    Complete integration test:
    - Creation of an Address
    - Creation of a Letting related to this Address
    - Verification in the index and detail view
    """
    second_address = Address.objects.create(
        number=456,
        street="Oak Street",
        city="Shelbyville",
        state="IL",
        zip_code=62565,
        country_iso_code="USA",
    )

    second_letting = Letting.objects.create(
        title="Luxury Villa",
        address=second_address
    )

    # Check that the letting is indeed accessible
    index_url = reverse("lettings_index")
    detail_url = reverse("letting", args=[second_letting.id])

    index_response = client.get(index_url)
    detail_response = client.get(detail_url)

    assert index_response.status_code == 200
    assert detail_response.status_code == 200
    assert "Luxury Villa" in index_response.content.decode()
    assert "456 Oak Street" in detail_response.content.decode()
