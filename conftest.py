import pytest
from django.contrib.auth.models import User

from lettings.models import Letting, Address
from profiles.models import Profile

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


@pytest.fixture
def user():
    """Fixture to create a Django user."""
    return User.objects.create_user(username="john_doe", password="password123")


@pytest.fixture
def profile(user):
    """Fixture to create a profile linked to the user."""
    return Profile.objects.create(user=user, favorite_city="Paris")


@pytest.fixture
def address():
    """Crée une adresse pour les tests d'intégration."""
    return Address.objects.create(
        number=123,
        street="Main Street",
        city="Springfield",
        state="IL",
        zip_code=62704,
        country_iso_code="USA",
    )


@pytest.fixture
def letting(address):
    """Crée un letting associé à une adresse."""
    return Letting.objects.create(
        title="Cozy Apartment",
        address=address
    )
