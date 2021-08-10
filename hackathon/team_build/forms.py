from django import forms
from .models import *

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['title', 'team_name', 'service', 
         'service_level', 'locate', 'team_members',
        'image', 'role', 'detail']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'recruit-title', 'placeholder': '제목'}),
            'team_name': forms.TextInput(attrs={'class': 'recruit-text-input', 'placeholder':'팀이름'}),
            'service': forms.TextInput(attrs={'class': 'recruit-text-input', 'placeholder':'서비스'}),
            'service_level': forms.Select(attrs={'class': 'recruit-select'}),
            'locate': forms.Select(attrs={'class': 'recruit-select'}),
            'team_members': forms.Select(attrs={'class': 'recruit-select'}),
            'role': forms.CheckboxSelectMultiple(attrs={'class': 'recruit-role'}),
            'image': forms.FileInput(attrs={'class': 'recruit-image'}),
            'detail': forms.Textarea(attrs={'class': 'recruit-detail'}),
        }

        labels = {
            'title': '제목:',
            'team_name': '팀명:',
            'service': '서비스:',
            'service_level': '서비스 단계:',
            'locate': '활동장소:',
            'team_members': '인원:',
            'role': '모집 포지션:',
            'image': '이미지:',
            'detail': '추가설명:',
        }
