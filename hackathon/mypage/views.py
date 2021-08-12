from scout.models import LikeUser
from django.shortcuts import get_object_or_404, redirect, render
from team_build.models import Recruit, Comment

from users.models import User
from team_build.models import LikeRecruit

def mypage(request, user_id):
    current_user = None
    if request.user.id:
        current_user = User.objects.get(pk=request.user.id)
    
    # 내가 쓴 글, 내가 쓴 댓글 불러오기
    my_recruits = Recruit.objects.filter(writer_username=request.user).order_by('-id')
    my_comments = Comment.objects.filter(user=request.user).order_by('-id')
    
    # 찜한 게시글 불러오기
    objects = LikeRecruit.objects.filter(user=user_id)
    recruits = []
    for obj in objects:
        recruits.append(Recruit.objects.get(pk=obj.recruit_key.id))
    # 중복 항목 제거
    recruits = list(dict.fromkeys(recruits))

    # 찜한 유저 불러오기
    objects = LikeUser.objects.filter(user=user_id)
    users = []
    for obj in objects:
        users.append(User.objects.get(pk=obj.user_key.id))
    users = list(dict.fromkeys(users))

    context = {
        'current_user':current_user,
        'my_recruits':my_recruits,
        'my_comments':my_comments,
        'recruits':recruits,
        'users':users,
    }
    return render(request, 'mypage/mypage.html', context)
