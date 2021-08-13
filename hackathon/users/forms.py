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

class CustomRegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget = forms.PasswordInput(attrs={'class':'password1-input1', 'placeholder':'8글자 이상. 숫자로만 입력할 수 없음'}))
    password2 = forms.CharField(max_length=16, widget = forms.PasswordInput(attrs={'class':'password2-input1', 'placeholder':'비밀번호 재입력'}))
    class Meta:
        model = User
        fields = ['name', 'image', 'username', 'password1', 'password2',
        'birth_date', 'address_sido','address_gungu',
        'career', 'state', 'role', 'intro']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'id-input1', 'placeholder': '150 글자 이하의 문자, 숫자 및 @ / . / + / - / _ 조합'}),
            # 'password1': forms.PasswordInput(attrs={'class':'password1-input1', 'placeholder':'8글자 이상. 숫자로만 입력할 수 없음'}), 
            # 'password2': forms.PasswordInput(attrs={'class':'password2-input1', 'placeholder':'비밀번호 재입력'}),
            'image': forms.ClearableFileInput(attrs={'class': 'image-input1', 'placeholder': ''}), 
            'name': forms.TextInput(attrs={'class': 'name-input1', 'placeholder': ''}), 
            'birth_date': forms.DateInput(attrs={'class': 'birthday-input1', 'placeholder': ''}), 
            'address_sido': forms.Select(attrs={'class': 'sido-input2', 'placeholder': ''}),
            'address_gungu': forms.TextInput(attrs={'class': 'gungu-input2', 'placeholder': '00군 혹은 00구'}),
            'career': forms.Select(attrs={'class': 'career-input2', 'placeholder': ''}),
            'state': forms.Select(attrs={'class': 'state-input2', 'placeholder': ''}), 
            'role': forms.CheckboxSelectMultiple(attrs={'class': 'role-input2', 'placeholder': ''}),
            'intro': forms.Textarea(attrs={'class': 'intro-input3', 'placeholder': '간단하게 자신을 나타내는 소개글을 적어주세요'})
        }

        labels = {
            'username': 'ID',
            'password1': '비밀번호', 
            'password2': '비밀번호 재입력',
            'image': '프로필 사진', 
            'name': '이름', 
            'birth_date': '생년월일', 
            'address_sido': '주소(시/도)',
            'address_gungu': '주소(군/구)',
            'career': '경력',
            'state': '상태', 
            'role': '희망포지션',
            'intro': '한줄소개'
        }

        # def __init__(self, *args, **kwargs):
        #     super(CustomRegisterForm, self).__init__(*args, **kwargs)
        #     self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'password1-input1', 'placeholder':'8글자 이상. 숫자로만 입력할 수 없음'})
        #     self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'password2-input1', 'placeholder':'비밀번호 재입력'})


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