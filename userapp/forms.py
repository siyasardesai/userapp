from django.forms import ModelForm
from django import forms

from .models import UserDetails

class UserForm(ModelForm):
    class Meta:
        model=UserDetails

