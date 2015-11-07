from django import forms
from .models import *


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

