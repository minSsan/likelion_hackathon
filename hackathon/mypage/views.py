from django.shortcuts import render
from team_build.models import Recruit, Comment

def mypage(request, user_id):
    # 내가 쓴 글, 내가 쓴 댓글 불러오기
    my_recruits = Recruit.objects.filter(writer=request.user).order_by('-id')
    my_comments = Comment.objects.filter(user_username=request.user).order_by('-id')
    context = {
        'my_recruits':my_recruits,
        'my_comments':my_comments,
    }
    return render(request, 'mypage/mypage.html', context)