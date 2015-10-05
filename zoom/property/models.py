from django.db import models
from accessibilityneed.models import AccessibilityNeed

# Create your models here.


class DomicileType(models.Model):
    """ This table distinguishes the type of housing it is"""
    name = models.CharField(max_length=200, default=None)


class Address(models.Model):
    """ This table holds the location of the property listing"""
    street = models.CharField(max_length=200, default=None)
    street_two = models.CharField(max_length=200, default=None)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    zip_code = models.CharField(max_length=50, default=None)


class Photo(models.Model):
    """ This table holds all the photos for the property"""
    photo = models.ImageField()


class Amenity(models.Model):
    """ This table holds all the amenities a property has """
    type = models.CharField(max_length=500, default=None)


class PotentialAllergen(models.Model):
    """ This table stores information on potential allergens"""

    description = models.CharField(max_length=500, default=None)


class Property(models.Model):
    """ This table holds information about each property """

    type_id = models.ForeignKey(DomicileType)
    address = models.ForeignKey(Address)
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=2000, default=None)
    num_bedroom = models.CharField(max_length=20, default=None)
    num_bathroom = models.CharField(max_length=20, default=None)
    # do I want to put num_access_bedroom, too?
    photo_property = models.ManyToManyField(Photo)
    property_amenity = models.ManyToManyField(Amenity)
    property_allergens = models.ManyToManyField(PotentialAllergen)


class Exceptions(models.Model):
    """ This tables holds exceptions to access needs"""
    need = models.CharField(max_length=200, default=None)
    room_location = models.CharField(max_length=200, default=None)


class PropertyNeed(models.Model):
    """ This table holds specific needs to a property """

    property_id = models.ForeignKey(Property)
    accessibility_need = models.ForeignKey(AccessibilityNeed)
    property_need = models.ManyToManyField(Exceptions)


class Vehicle(models.Model):
    """ This table holds a list of possible vehicle availability """

    property_id = models.ForeignKey(Property)
    make = models.CharField(max_length=50, default=None)
    model = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=500, default=None)
    access_needs = models.ManyToManyField(AccessibilityNeed)




