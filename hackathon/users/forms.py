from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
        'image', 'name', 'birth_date', 'address_sido',
        'address_gungu','career', 'state', 'role',
        'intro']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'id-input', 'placeholder': '아이디'}),
            'password': forms.PasswordInput(attrs={'class':'password-input', 'placeholder':'비밀번호'}),
        }
        labels = {
            'username':'아이디',
            'password':'비밀번호',
        }