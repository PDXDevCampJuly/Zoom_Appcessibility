from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DomicileType(models.Model):
    """ This table distinguishes the type of housing it is"""
    name = models.CharField(max_length=200, default=None)
    house = models.BooleanField(default=False)
    apartment = models.BooleanField(default=False)
    condo = models.BooleanField(default=False)
    loft = models.BooleanField(default=False)
    square_feet = models.BooleanField(default=False)


class Address(models.Model):
    """ This table holds the location of the a_zoom_world listing"""
    street = models.CharField(max_length=200, default=None)
    street_two = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    zip_code = models.IntegerField()


class Photo(models.Model):
    """ This table holds all the photos for the a_zoom_world"""
    photo = models.ImageField(upload_to='images/')


class Amenity(models.Model):
    """ This table holds all the amenities a a_zoom_world has """
    type = models.CharField(max_length=500, default=None)
    washer = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)
    service_dog = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    hot_tub = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    microwave = models.BooleanField(default=False)
    coffee = models.BooleanField(default=False)
    tea = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    cookware = models.BooleanField(default=False)
    utensils = models.BooleanField(default=False)


class PotentialAllergen(models.Model):
    """ This table stores information on potential allergens"""

    description = models.CharField(max_length=500, default=None)
    cedar_trees = models.BooleanField(default=False)
    cats_inside = models.BooleanField(default=False)
    dogs_inside = models.BooleanField(default=False)


class Property(models.Model):
    """ This table holds information about each a_zoom_world """

    type_id = models.ForeignKey(DomicileType)
    address = models.ForeignKey(Address)
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=2000, default=None)
    num_bedroom = models.CharField(max_length=20, default=None)
    num_bathroom = models.CharField(max_length=20, default=None)
    # do I want to put num_access_bedroom, too?
    photo_property = models.ManyToManyField(Photo, related_name='property_photos', verbose_name=('photo_property'))
    property_amenity = models.ManyToManyField(Amenity)
    property_allergens = models.ManyToManyField(PotentialAllergen)


class NeedException(models.Model):
    """ This tables holds exceptions to access needs"""
    need = models.CharField(max_length=200, default=None)
    room_location = models.CharField(max_length=200, default=None)


class AccessibilityNeed(models.Model):
    """ This table holds the list of accessibility needs for the user/traveller"""

    name = models.CharField(max_length=200, default=None)
    description = models.CharField(max_length=1000, default=None)


class Vehicle(models.Model):
    """ This table holds a list of possible vehicle availability """

    property_id = models.ForeignKey(Property)
    make = models.CharField(max_length=50, default=None)
    model = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=500, default=None)
    access_needs = models.ManyToManyField(AccessibilityNeed)


class PropertyNeed(models.Model):
    """ This table holds specific needs to a listed property  """

    property_id = models.ForeignKey(Property)
    accessibility_need = models.ForeignKey(AccessibilityNeed)
    property_need = models.ManyToManyField(NeedException)
    roll_in_shower = models.BooleanField(default=False)
    grab_rails_in_bathroom = models.BooleanField(default=False)
    visual_impairment = models.BooleanField(default=False)
    hearing_impairment = models.BooleanField(default=False)
    wheelchair_scooter_access = models.BooleanField(default=False)
    electric_bed = models.BooleanField(default=False)
    shower_chair = models.BooleanField(default=False)
    ceiling_track_hoist = models.BooleanField(default=False)
    mobile_hoist = models.BooleanField(default=False)
    pool_hoist = models.BooleanField(default=False)


class ZoomUser(models.Model):
    """ This table holds the user information using django default"""

    user = models.OneToOneField(User)
    accessibility_need = models.ForeignKey(AccessibilityNeed)

