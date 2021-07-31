from django import forms
from .models import *

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['title', 'team_name', 'service', 
        'team_members', 'service_level', 'locate', 
        'image', 'role', 'detail', 'founding_date']
