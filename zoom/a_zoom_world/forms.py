from django import forms
from .models import *


class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['wifi', 'washer/dryer', '',]


class PropertyAccessibilityForm(forms.ModelForm):
    class Meta:
        model = PropertyNeed
        fields = ['roll_in_shower', ]
