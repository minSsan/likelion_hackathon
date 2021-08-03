from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Q

from users.models import User

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