from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *

from django.core.paginator import Paginator
from django.db.models import Q

import json

def main(request):
    return render(request, 'main.html')

def team_build(request):
    recruit_posts = Recruit.objects.all()
    context = {
        'posts':recruit_posts,
    }
    return render(request, 'team_build.html', context)

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
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

# 팀원 모집글 작성하기
def create_recruit(request):
    recruits_form = RecruitForm()
    if request.method == "POST":
        recruits_form = RecruitForm(request.POST, request.FILES)

        if recruits_form.is_valid():
            username = request.user
            new_form = recruits_form.save(commit=False)
            new_form.writer = get_object_or_404(User, username=username).name
            new_form.writer_username = username
            new_form.save()
        return redirect('main')
    else:
        context = {
            'form': recruits_form,
        }
        return render(request, 'create_recruit.html', context)

# 팀원 모집글 자세히 보기
def detail_recruit(request, id):
    recruit_instance = get_object_or_404(Recruit, pk=id)
    comments_instance = Comment.objects.filter(recruit_id=id).order_by('-id')
    ans_comment_instance = CommentAnswer.objects.all()

    paginator = Paginator(comments_instance, 6)
    page = request.GET.get('page')
    comments = paginator.get_page(page)


    context ={
        'obj': recruit_instance,
        'id': id,
        'comments': comments,
        'ans_comments':ans_comment_instance,
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
        # 폼 생성 및 요청에 의한 데이터로 채우기
        recruit_update_form = RecruitForm(request.POST, request.FILES, instance=recruit_instance)

        # 폼이 유효한가?
        if recruit_update_form.is_valid():
            # 데이터를 요청받은 내용으로 처리
            recruit_update_form.save()
        return redirect('main')

    else:
        form = RecruitForm(instance=recruit_instance)
        context = {
        'form': form,
        'id': id,
        }
        return render(request, 'update_recruit.html', context)

# 모집글 댓글
def create_comment(request, id):
    username = request.user
    
    if json.loads(request.body).get('answer_comment') == 'True':
        new_comment = CommentAnswer()
        new_comment.comment_id = Comment.objects.get(pk=json.loads(request.body).get('comment_id'))
        
    else:
        new_comment = Comment()
        new_comment.recruit_id = Recruit.objects.get(pk=id)

    new_comment.content = json.loads(request.body).get('text')
    new_comment.user = get_object_or_404(User, username=username).name
    new_comment.user_username = username
    new_comment.pub_date = timezone.now()
    new_comment.save()
    
    return redirect('detail_recruit', id)

def update_comment(request, id, comment_id):
    if json.loads(request.body).get('answer_comment') == "False":
        comment_instance = get_object_or_404(Comment, id=comment_id)
    else:
        comment_instance = get_object_or_404(CommentAnswer, id=comment_id)
    
    comment_instance.content = json.loads(request.body).get('text')
    comment_instance.save()
    
    return redirect('detail_recruit', id)

def delete_comment(request, id, comment_id):
    # 해당 댓글 불러오기
    comment_instance = get_object_or_404(Comment, pk=comment_id)

    # 댓글 작성자랑 로그인 유저랑 같으면
    if str(request.user) == comment_instance.user_username:
        comment_instance.delete()

    return redirect('detail_recruit', id)

# 프로필 페이지
def profile(request, id):
    user_instance = get_object_or_404(User, pk=id)
    pfs = Portfolio.objects.filter(user_id=id)
    context = {
        'user_id':id,
        'obj': user_instance,
        'pfs':pfs,
    }
    return render(request, 'profile.html', context)

def detail_portfolio(request, user_id, pf_id):
    portfolio = get_object_or_404(Portfolio, pk=pf_id)
    context = {
        'pf':portfolio,
        'user_id':user_id,
        'pf_id':pf_id,
    }
    return render(request, 'detail_pf.html', context)

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
    if request.method == "POST":
        update_form = PortfolioForm(request.POST, request.FILES, instance=pf_instance)
        if update_form.is_valid():
            update_form.save()
        return redirect('profile', user_id)
    else:
        update_form = PortfolioForm(instance=pf_instance)
        context = {
            'form':update_form,
            'user_id':user_id,
            'pf_id':pf_id,
        }
        return render(request, 'update_pf.html', context)

# 게시글 검색 기능
def recruit_role_search(request, input_role):
    results = Recruit.objects.filter(Q(role__icontains=input_role)).distinct()
    # distinct() : 중복된 객체 제외
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts':posts,
    }
    return render(request, 'recruit_role_search.html', context)


# 유저 검색 기능 ( 아직 역할 검색만 )
def user(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user.html', context)

def user_search(request, input_role):
    results = User.objects.filter(Q(role__icontains=input_role))
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context = {
        'users':users,
    }
    return render(request, 'user_search.html', context)

def user_search_text(request, input_text):

    results = User.objects.filter((Q(name__icontains=input_text) | Q(address_sido__icontains=input_text) | Q(address_gungu__icontains=input_text) | Q(career__icontains=input_text)))
    paginator = Paginator(results, 10)
    print(User.objects.filter(Q(name__icontains=input_text) & Q(address_sido__icontains=input_text) & Q(address_gungu__icontains=input_text)))
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context = {
        'users':users,
    }
    return render(request, 'user_search.html', context)


