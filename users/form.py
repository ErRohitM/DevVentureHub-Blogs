from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bloger

class BlogerRegistrationForm(UserCreationForm):
    
    class Meta:
        model = Bloger
        fields = ('username', 'bloger_email', 'contact_info')
