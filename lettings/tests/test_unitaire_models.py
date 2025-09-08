import pytest
from django.core.exceptions import ValidationError

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_creation(address):
    """Test the creation of an Address instance and its fields."""
    saved_address = Address.objects.get(id=address.id)

    assert saved_address.number == 123
    assert saved_address.street == "Main Street"
    assert saved_address.city == "Springfield"
    assert saved_address.state == "IL"
    assert saved_address.zip_code == 62704
    assert saved_address.country_iso_code == "USA"


@pytest.mark.django_db
def test_address_str_method(address):
    """Test the string representation of Address."""
    assert str(address) == "123 Main Street"


def test_meta_verbose_names():
    assert Address._meta.verbose_name == "Address"
    assert Address._meta.verbose_name_plural == "Addresses"


@pytest.mark.django_db
def test_number_validators_max_value(address):
    # Number too large
    address.number = 10000  # > 9999

    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_state_validators_max_length(address):
    # State code too long
    address.state = "FRA"  # > 2

    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_state_validators_min_length(address):
    # State code Too short
    address.state = "F"  # < 2

    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_zip_code_validators_max_value(address):
    # Zip_code too large
    address.zip_code = 100000,  # > 99999

    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_country_iso_code_validators_min_value(address):
    # country_iso_code too short
    address.country_iso_code = "F"  # < 3

    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_country_iso_code_validators_max_value(address):
    # country_iso_code too long
    address.country_iso_code = "FRAN",  # > 3

    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_letting_creation_with_address(letting, address):
    """Test creation of a Letting with an Address relationship."""

    saved_letting = Letting.objects.get(id=letting.id)

    assert saved_letting.title == "Cozy Apartment"
    assert saved_letting.address == address


@pytest.mark.django_db
def test_letting_str_method(letting):
    """Test the string representation of Letting."""
    assert str(letting) == "Cozy Apartment"


@pytest.mark.django_db
def test_profile_deleted_when_user_deleted(address, letting):
    """Checks that the deletion of a address removes the associated letting."""
    address.delete()
    assert Letting.objects.count() == 0
