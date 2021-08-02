from django import forms
from django.db.models import fields
from django.db.models.base import Model

from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget

from .models import *

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'detail']
        widgets = {
            'detail': SummernoteWidget(),
        }

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['title', 'team_name', 'service', 
        'team_members', 'service_level', 'locate', 
        'image', 'role', 'detail', 'founding_date']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 
        'name', 'birth_date', 'address_sido', 'address_gungu',
        'career', 'state', 'role']
