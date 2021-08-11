from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from .models import *
from .forms import *

###### 로그인 페이지 ######
# 로그인 페이지, 로그인 기능 #
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid(): # 유효성 검사
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return HttpResponse('입력 정보가 올바르지 않습니다.')
        return redirect("main:main")
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})

# 로그아웃 #
def logout_view(request):
    logout(request)
    return redirect("main:main")

# 회원가입 페이지, 회원가입 기능 #
def signup_view(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main:main")
    else:
        form = CustomRegisterForm()
        return render(request, 'users/signup.html', {'form': form})
