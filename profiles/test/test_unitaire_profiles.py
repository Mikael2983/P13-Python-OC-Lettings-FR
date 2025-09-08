import pytest

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_creation(profile):
    """Checks that a profile is correctly created."""
    assert profile.user.username == "john_doe"
    assert profile.favorite_city == "Paris"
    assert isinstance(profile, Profile)


@pytest.mark.django_db
def test_profile_str_method(profile):
    """Verify that __str__ returns the username."""
    assert str(profile) == "john_doe"


@pytest.mark.django_db
def test_favorite_city_can_be_blank(user):
    """Check that favorite_city can be empty."""
    profile = Profile.objects.create(user=user, favorite_city="")
    assert profile.favorite_city == ""


@pytest.mark.django_db
def test_profile_deleted_when_user_deleted(user, profile):
    """Checks that the deletion of a User removes the associated Profile."""
    user.delete()
    assert Profile.objects.count() == 0
