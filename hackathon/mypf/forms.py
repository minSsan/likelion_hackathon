from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import *

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'image', 'detail']
        widgets = {
            'detail': SummernoteWidget(),
        }