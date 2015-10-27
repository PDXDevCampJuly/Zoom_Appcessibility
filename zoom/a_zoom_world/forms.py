from django import forms
from .models import *


# class AmenityForm(forms.ModelForm):
#     class Meta:
#         model = Amenity
#         fields = ['washer', 'dryer', 'service_dog', 'pets', 'internet', 'parking', 'tv',
#                   'pool','hot_tub','gym', 'fridge', 'microwave','coffee', 'tea',
#                   'restaurant', 'cookware','utensils']


# class PropertyAccessibilityForm(forms.ModelForm):
#     class Meta:
#         model = PropertyNeed
#         fields = ['roll_in_shower', 'grab_rails_in_bathroom','visual_impairment',
#                   'hearing_impairment', 'wheelchair_scooter_access', 'electric_bed',
#                   'shower_chair', 'ceiling_track_hoist', 'mobile_hoist',
#                   'pool_hoist']


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


# class AllergenForm(forms.ModelForm):
#     class Meta:
#         model = PotentialAllergen
#         fields = ['cedar_trees', 'cats_inside', 'dogs_inside']


# class PropertyType(forms.ModelForm):
#     class Meta:
#         model = DomicileType
#         fields = ['house', 'apartment', 'condo', 'loft', 'square_feet']
