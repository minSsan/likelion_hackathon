from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 
        'name', 'birth_date', 'address_sido', 'address_gungu',
        'career', 'state', 'role', 'intro']