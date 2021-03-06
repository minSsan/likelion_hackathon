from django.contrib import messages
from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from django.db.models import Q

from users.models import User
from .models import LikeUser

PAGE_RANGE = 5

LIST_RANGE = 12

# 유저 검색 기능 ( 아직 역할 검색만 )
def user(request):
    if request.user.id:
        user_instance = User.objects.get(pk=request.user.id)
    else:
        user_instance = None

    users = User.objects.all().order_by('-id')
    max_index = len(users) / LIST_RANGE

    paginator = Paginator(users, LIST_RANGE)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    # max_index = len(paginator.page_range)

    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / PAGE_RANGE) * PAGE_RANGE
    end_index = start_index + PAGE_RANGE
    if end_index >= max_index:
        end_index = max_index

    page_range = []
    for index in range(int(start_index), int(end_index) + 1):
        page_range.append(index + 1)

    context = {
        'current_user':user_instance,
        'users': users,
        'page_range':page_range,
    }
    return render(request, 'scout/user.html', context)

def user_search(request, input_role):
    current_user = None
    if request.user.id:
        current_user = User.objects.get(pk=request.user.id)
    
    results = User.objects.filter(Q(role__icontains=input_role)).order_by('-id')
    max_index = len(results) / LIST_RANGE

    paginator = Paginator(results, LIST_RANGE)
    page = request.GET.get('page')
    users = paginator.get_page(page)

    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / PAGE_RANGE) * PAGE_RANGE
    end_index = start_index + PAGE_RANGE
    if end_index >= max_index:
        end_index = max_index
    
    page_range = []
    for index in range(int(start_index), int(end_index) + 1):
        page_range.append(index + 1)
    
    context = {
        'current_user':current_user,
        'users':users,
        'page_range':page_range,
    }
    return render(request, 'scout/user_search.html', context)

def user_search_text(request, input_text):
    if len(input_text) <= 1:
        messages.error(request, '두 글자 이상 입력해주세요.')

    results = User.objects.filter(
        Q(name__icontains=input_text) | 
        Q(address_sido__icontains=input_text) | 
        Q(address_gungu__icontains=input_text) | 
        Q(career__icontains=input_text) |
        Q(state__icontains=input_text)
        ).order_by('-id')
    max_index = len(results) / LIST_RANGE

    paginator = Paginator(results, LIST_RANGE)
    # print(User.objects.filter(Q(name__icontains=input_text) & Q(address_sido__icontains=input_text) & Q(address_gungu__icontains=input_text)))
    page = request.GET.get('page')
    users = paginator.get_page(page)

    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / PAGE_RANGE) * PAGE_RANGE
    end_index = start_index + PAGE_RANGE
    if end_index >= max_index:
        end_index = max_index
    
    page_range = []
    for index in range(int(start_index), int(end_index) + 1):
        page_range.append(index + 1)

    context = {
        'users':users,
        'page_range':page_range,
    }
    return render(request, 'scout/user_search.html', context)

###### 찜 기능 ######
# 찜하기 버튼 누를 때
def user_like(request, user_id):
    like_object = LikeUser.objects.filter(user=request.user.id, user_key=user_id)
    if like_object:
        like_object.delete()
    else:
        like_object = LikeUser()
        like_object.user = request.user.id
        like_object.user_key = User.objects.get(pk=user_id)
        like_object.save()
    return redirect('scout:user')