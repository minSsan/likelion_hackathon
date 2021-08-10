from django import forms
from django.forms.widgets import FileInput
from django_summernote.widgets import SummernoteWidget

from .models import *

# class PortfolioForm(forms.ModelForm):
#     class Meta:
#         model = Portfolio
#         fields = ['title', 'image', 'detail']
#         widgets = {
#             'detail': SummernoteWidget(),
#         }

class CustomPortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'image', 'detail']
        widgets = {
            'title': forms.TextInput(attrs={'class':'title-input', 'placeholder':'모집목적에 맞는 제목을 써주세요.'}),
            'image': forms.FileInput(),
            'detail': SummernoteWidget(),
        }
        labels = {
            'title':'제목',
            'image':'썸네일',
            'detail':'내용',
        }