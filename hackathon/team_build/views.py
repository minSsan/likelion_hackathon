from django.http.response import HttpResponse, HttpResponseRedirect
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from users.models import User
from .models import LikeRecruit
from .forms import *

from django.views.generic import ListView

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

import json


###### 팀 빌딩 페이지 ######
# 1. 팀빌딩 메인 
#    팀빌딩 키워드 검색 기능 -> query 방식 #
class RecruitListView(ListView):
    model = Recruit
    paginate_by = 5
    # 리스트를 team_build.html 템플릿으로 보낼 것임
    template_name = 'team_build/team_build.html'
    # 템플릿에서 리스트를 호출할 때 'recruit_list'로 호출
    context_object_name = 'recruit_list'

    def get_queryset(self):
        # 사용자가 입력한 검색어를 저장 -> GET 방식, 검색 input태그 name == 'q'
        # q 라는 파라미터에 할당된 값을 불러옴
        search_word = self.request.GET.get('q','')
        
        # 검색어가 포함된 게시글 리스트를 저장할 변수
        recruit_list = Recruit.objects.all()

        if search_word: # 만약 검색어가 존재하는 경우
            if len(search_word) > 1: # 두 글자 이상
                recruit_list = recruit_list.filter(
                    Q(title__icontains=search_word) | 
                    Q(writer__icontains=search_word) |
                    Q(team_name__icontains=search_word) |
                    Q(service__icontains=search_word) |
                    Q(detail__icontains=search_word)
                    )
                recruit_list = recruit_list.order_by('-id')
                return recruit_list
            else:
                messages.error(self.request, '두 글자 이상 입력해주세요.')
        # 검색어가 없는 기본 상태일 때는, 모든 Recruit 객체 리스트를
        # recruit_list에 담아서 반환
        # id 내림차순 -> 최신순으로 나열
        recruit_list = recruit_list.order_by('-id')
        return recruit_list

    # context에 리스트뿐만 아니라, 추가적으로 정보를 더 담는 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        # 페이지 이동 버튼에서 최대 5개의 페이지만 띄울 것임
        page_num_range = 5
        max_index = len(paginator.page_range)

        # 현재 페이지 정보를 불러옴
        page = self.request.GET.get('page')
        # 현재 페이지 정보가 0이면 curreunt_page를 1로 저장
        current_page = int(page) if page else 1
        # 
        start_index = int((current_page - 1) / page_num_range) * page_num_range
        end_index = start_index + page_num_range
        if end_index >= max_index:
            end_index = max_index
        
        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

# 2. 팀빌딩 직무 검색 기능 #
def recruit_role_search(request, input_role):
    results = Recruit.objects.filter(Q(role__icontains=input_role)).distinct()
    results = results.order_by('-id')
    # distinct() : 중복된 객체 제외
    paginator = Paginator(results, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts':posts,
    }
    return render(request, 'team_build/recruit_role_search.html' ,context)

# 2-1. 팀 빌딩 지역 검색 기능 #
def recruit_location_search(request, input_location):
    results = Recruit.objects.filter(locate=input_location).distinct()
    paginator = Paginator(results, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts':posts,
    }
    return render(request, 'team_build/recruit_location_search.html', context)

# 3. 팀빌딩 글 작성 페이지, 기능 #
def create_recruit(request):
    recruits_form = RecruitForm()
    if request.method == "POST":
        recruits_form = RecruitForm(request.POST, request.FILES)
        # 유효성 검사 통과 안 됨 => 수정 필요
        if recruits_form.is_valid():
            new_form = recruits_form.save(commit=False)
            new_form.writer = request.user.name
            new_form.writer_username = request.user
            new_form.save()
        return redirect('team_build:team_build')
    else:
        context = {
            'form': recruits_form,
        }
        return render(request, 'team_build/create_recruit.html', context)

# 4-1. 팀빌딩 게시글 자세히 보기 #
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
    return render(request, 'team_build/detail_recruit.html', context)

# 4-2. 팀빌딩 게시글 삭제하기 #
def delete_recruit(request, id):
    # 해당 게시글 불러오기
    recruit_instance = get_object_or_404(Recruit, pk=id)

    # 게시글 작성자랑 로그인 유저랑 같으면
    if str(request.user) == recruit_instance.writer_username:
        recruit_instance.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('team_build:team_build')
    else:
        messages.error(request, "타인이 작성한 게시글은 삭제할 수 없습니다.")
        return redirect('team_build:detail_recruit', id)

# 4-3. 팀빌딩 게시글 수정하기 #
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
        return redirect('team_build:team_build')

    else:
        form = RecruitForm(instance=recruit_instance)
        context = {
        'form': form,
        'id': id,
        }
        return render(request, 'team_build/update_recruit.html', context)




###### 모집글 댓글 ######
# 1. 댓글 작성
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
    
    return HttpResponse(status=200)

# 2. 댓글 수정
def update_comment(request, id, comment_id):
    if json.loads(request.body).get('answer_comment') == "False":
        comment_instance = get_object_or_404(Comment, id=comment_id)
    else:
        comment_instance = get_object_or_404(CommentAnswer, id=comment_id)
    
    comment_instance.content = json.loads(request.body).get('text')
    comment_instance.save()
    
    return HttpResponse(status=200)

# 3. 댓글 삭제
def delete_comment(request, id, comment_id, answer_comment):
    # 해당 댓글 불러오기
    if answer_comment == 'False':
        comment_instance = get_object_or_404(Comment, pk=comment_id)
    else:
        comment_instance = get_object_or_404(CommentAnswer, pk=comment_id)
        
    # 댓글 작성자랑 로그인 유저랑 같으면
    if str(request.user) == comment_instance.user_username:
        comment_instance.delete()

    print(id)

    return HttpResponse(status=200)


###### 찜 기능 ######
# 찜하기 버튼 누를 때 실행
def recruit_like(request, recruit_id):
    like_object = LikeRecruit.objects.filter(user=request.user.id, recruit_key=recruit_id)
    # 만약 이미 찜이 되어있는 상태라면,(=찜 해제 버튼을 누른 경우)
    if like_object:
        # 찜 해제(테이블 삭제)
        like_object.delete()
    # 해당 테이블이 없는 경우(=찜 목록에 없는 경우, =찜하기 버튼을 누른 경우)
    else:
        # 찜 설정(테이블 생성)
        like_object = LikeRecruit()
        like_object.user = request.user.id
        like_object.recruit_key = Recruit.objects.get(pk=recruit_id)
        like_object.save()
    return redirect('team_build:team_build')