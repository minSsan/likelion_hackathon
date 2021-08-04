from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from django.db.models import Q

from users.models import User
from .models import LikeUser

# 유저 검색 기능 ( 아직 역할 검색만 )
def user(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'scout/user.html', context)

def user_search(request, input_role):
    results = User.objects.filter(Q(role__icontains=input_role))
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context = {
        'users':users,
    }
    return render(request, 'scout/user_search.html', context)

def user_search_text(request, input_text):
    results = User.objects.filter((Q(name__icontains=input_text) | Q(address_sido__icontains=input_text) | Q(address_gungu__icontains=input_text) | Q(career__icontains=input_text)))
    paginator = Paginator(results, 10)
    print(User.objects.filter(Q(name__icontains=input_text) & Q(address_sido__icontains=input_text) & Q(address_gungu__icontains=input_text)))
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context = {
        'users':users,
    }
    return render(request, 'scout/user_search.html', context)

###### 찜 기능 ######
# 찜하기 버튼 누를 때
def create_like(request, user_id):
    like_object = LikeUser()
    like_object.user = request.user.id
    like_object.user_key = User.objects.get(pk=user_id)
    like_object.save()
    return redirect('scout:user')

# 찜 해제 버튼 누를 때
def delete_like(request, user_id):
    like_object = LikeUser.objects.filter(user=request.user.id, user_key=user_id)
    if like_object:
        like_object.delete()
    return redirect('scout:user')