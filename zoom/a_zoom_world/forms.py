from django import forms
from .models import *


class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['Washer/Dryer', 'Pet Friendly', 'Internet', 'Parking', 'TV',
                  'Swimming Pool','Hot Tub','Gym', 'Fridge', 'Microwave','Coffee/Tea',
                  'Restaurant', 'Cookware/Utensils',]


class PropertyAccessibilityForm(forms.ModelForm):
    class Meta:
        model = PropertyNeed
        fields = ['roll_in_shower', 'Grab Rails in Bathroom','Visual Impairment',
                  'Hearing Impairment', 'WheelChair/Scooter Access', 'Electric Bed',
                  'Shower Chair', 'Ceiling Track Hoist', 'Mobile Hoist',
                  'Pool Hoist',]


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password',]


class AllergenForm(forms.ModelForm):
    class Meta:
        model = PotentialAllergen
        fields = ['Cedar Trees', 'Cats Inside', 'Dogs Inside',]


class PropertyType(forms.ModelForm):
    class Meta:
        model = DomicileType
        fields = ['House', 'Apartment', 'Condo', 'Loft', 'Square Feet',]
