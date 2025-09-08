"""
Models for managing property lettings and their associated addresses.

This module defines the database schema for storing information
about addresses and property lettings in the application.

Classes:
    Address:
        Represents a postal address with number, street, city, state,
        zip code, and country ISO code.

    Letting:
        Represents a property letting with a title and associated address.

The models use Django's ORM for database interaction and include
validation rules for field values.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a postal address.

    Attributes:
        number (PositiveIntegerField): Street number, must be between 1 and
            9999.
        street (CharField): Street name, up to 64 characters.
        city (CharField): City name, up to 64 characters.
        state (CharField): State code (2 characters), must be exactly 2
            characters.
        zip_code (PositiveIntegerField): Postal code, up to 5 digits.
        country_iso_code (CharField): Country ISO code (3 characters), must be
            exactly 3 characters.

    Meta:
        verbose_name (str): a singular name.
        verbose_name_plural (str): a plural name.

    Methods:
        __str__: Returns a string representation of the address in the format
            "<number> <street>".
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Return a readable string representation of the address.

        Returns:
            str: The address in the format "<number> <street>".
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a property letting.

    Attributes:
        title (CharField): The title or name of the letting, up to 256
            characters.
        address (OneToOneField): A one-to-one relationship to an Address
            instance, representing the location of the letting. Deleting the
            address will also delete the letting.

    Methods:
        __str__: Returns the title of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a readable string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
