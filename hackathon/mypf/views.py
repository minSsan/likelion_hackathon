from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator

from mypf.models import *
from users.models import User
from .forms import *

###### 마이페이지 ######
# 1. 마이페이지 불러오기 #
def profile(request, id):
    user_instance = User.objects.get(pk=request.user.id)
    user = get_object_or_404(User, pk=id)

    pfs = Portfolio.objects.filter(user_id=id).order_by('-id')
    paginator = Paginator(pfs, 4)
    page = request.GET.get('page')
    pfs = paginator.get_page(page)

    context = {
        'user_instance': user_instance,
        'user_id':id,
        'obj': user,
        'pfs':pfs,
    }
    return render(request, 'mypf/profile.html', context)

# 2. 포트폴리오 #
# 2-1. 포트폴리오 상세보기 # 
def detail_portfolio(request, user_id, pf_id):
    portfolio = get_object_or_404(Portfolio, pk=pf_id)
    context = {
        'pf':portfolio,
        'user_id':user_id,
        'pf_id':pf_id,
    }
    return render(request, 'mypf/detail_pf.html', context)

# 2-2. 포트폴리오 작성하기 #
def create_portfolio(request, user_id): # user id 필요
    form = PortfolioForm()
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            new_portfolio = form.save(commit=False)
            new_portfolio.user_id = User.objects.get(pk=user_id)
            new_portfolio.save()
        return redirect('mypf:profile', user_id) # 유저 페이지 redirect
    else:
        context = {
            'form':form,
            'user_id':user_id,
        }
        return render(request, 'mypf/create_pf.html', context)
    # 포트폴리오 생성 페이지를 렌더링할 때 username 함께 전달 
    # => Portfolio 모델에서 username 값을 필요로 하기 때문
    #   (=어느 회원의 포트폴리오인지 구분)

# 2-3. 포트폴리오 삭제하기 #
def delete_portfolio(request, user_id, pf_id):
    pf_instance = get_object_or_404(Portfolio, pk=pf_id)
    pf_instance.delete()
    return redirect('mypf:profile', user_id)

# 2-4. 포트폴리오 수정하기 #
def update_portfolio(request, user_id, pf_id):
    pf_instance = get_object_or_404(Portfolio, pk=pf_id)
    if request.method == "POST":
        update_form = PortfolioForm(request.POST, request.FILES, instance=pf_instance)
        if update_form.is_valid():
            update_form.save()
        return redirect('mypf:profile', user_id)
    else:
        update_form = PortfolioForm(instance=pf_instance)
        context = {
            'form':update_form,
            'user_id':user_id,
            'pf_id':pf_id,
        }
        return render(request, 'mypf/update_pf.html', context)