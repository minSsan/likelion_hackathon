from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import request
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .forms import *

def main(request):
    recruit_posts = Recruit.objects.all()
    context = {
        'posts':recruit_posts,
    }
    return render(request, 'main.html', context)

# 로그인
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid(): # 유효성 검사
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("main")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

# 로그아웃
def logout_view(request):
    logout(request)
    return redirect("main")

# 회원가입
def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
        return redirect("main")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

# 팀원 모집글 작성하기
def create_recruit(request):
    recruits_form = RecruitForm()
    context = {
        'form': recruits_form,
    }
    if request.method == "POST":
        form = RecruitForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.writer = request.user
            new_form.save()
        return redirect('main')
    else:
        return render(request, 'create_recruit.html', context)

# 팀원 모집글 자세히 보기
def detail_recruit(request, id):
    recruit_instance = get_object_or_404(Recruit, pk=id)
    context ={
        'obj': recruit_instance,
        'id': id,
    }
    return render(request, 'detail_recruit.html', context)

# 팀원 모집글 삭제하기
def delete_recruit(request, id):
    # 해당 게시글 불러오기
    recruit_instance = get_object_or_404(Recruit, pk=id)

    # 게시글 작성자랑 로그인 유저랑 같으면
    if str(request.user) == recruit_instance.writer:
        recruit_instance.delete()

    return redirect('main')

# 팀원 모집글 수정하기
def update_recruit(request, id):
    recruit_instance = get_object_or_404(Recruit, pk=id)
    
    # POST 요청
    if request.method == "POST":
        # # 폼 생성 및 요청에 의한 데이터로 채우기
        # recruit_update_form = RecruitForm(request.POST, request.FILES)

        # # 폼이 유효한가?
        # if recruit_update_form.is_valid():
        #     # 데이터를 요청받은 내용으로 처리
        #     recruit_instance = recruit_update_form
        #     recruit_instance.save()
        return redirect('main')

    else:
        form = RecruitForm()
        context = {
        'form': form,
        'id': id,
        }
        return render(request, 'update_recruit.html', context)

# 프로필 페이지
def profile(request, id):
    user_instance = get_object_or_404(User, pk=id)
    pfs = Portfolio.objects.filter(user_id=id)
    context = {
        'obj': user_instance,
        'pfs':pfs,
    }
    return render(request, 'profile.html', context)

# user 마이페이지 뷰 구현 
# -> user id 받아와서 포트폴리오 스마트 에디터 기능 작동 확인 / 반환값 형태 확인

def create_portfolio(request, user_id): # user id 필요
    form = PortfolioForm()
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            new_portfolio = form.save(commit=False)
            new_portfolio.user_id = User.objects.get(pk=user_id)
            new_portfolio.save()
        return redirect('profile', user_id) # 유저 페이지 redirect
    else:
        context = {
            'form':form,
            'user_id':user_id,
        }
        return render(request, 'create_pf.html', context)
    # 포트폴리오 생성 페이지를 렌더링할 때 username 함께 전달 
    # => Portfolio 모델에서 username 값을 필요로 하기 때문
    #   (=어느 회원의 포트폴리오인지 구분)

def delete_portfolio(request, user_id, pf_id):
    pf_instance = get_object_or_404(Portfolio, pk=pf_id)
    pf_instance.delete()
    return redirect('profile', user_id)

def update_portfolio(request, user_id, pf_id):
    pf_instance = get_object_or_404(Portfolio, pk=pf_id)
