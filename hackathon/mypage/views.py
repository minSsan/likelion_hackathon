from django.shortcuts import get_object_or_404, redirect, render
from team_build.models import Recruit, Comment
from users.models import User
from .models import LikeRecruit

def mypage(request, user_id):
    # 내가 쓴 글, 내가 쓴 댓글 불러오기
    my_recruits = Recruit.objects.filter(writer=request.user).order_by('-id')
    my_comments = Comment.objects.filter(user_username=request.user).order_by('-id')
    
    # 찜한 게시글 불러오기
    user_obj = User.objects.get(pk=user_id)
    objects = LikeRecruit.objects.filter(user=user_obj)
    recruits = []
    for obj in objects:
        recruits.append(Recruit.objects.get(pk=obj.recruit_key.id))
    # 중복 항목 제거
    recruits = list(dict.fromkeys(recruits))
    context = {
        'my_recruits':my_recruits,
        'my_comments':my_comments,
        'recruits':recruits,
    }
    return render(request, 'mypage/mypage.html', context)