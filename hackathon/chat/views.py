# chat/views.py
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.db.models import Prefetch, Q

import sys, os, json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('users'))))
from users import models

# custom function
def create_room_id(num1, num2):
    if num1 < num2:
        id = num1 + "id" + num2
        return id
    else:
        id = num2 + "id" + num1
        return id

def opp_name(my_name, obj_list):
    array = []
    for obj in obj_list:
        for str in obj.title.split(', '):
            if my_name != str:
                array.append(str)
    return array

def chat_recent(obj, chat_room):
    return obj.objects.filter(chat_room_id=chat_room).order_by('-id')[0].chat_text

def opp_id(my_id, chat_room_id):
    array = chat_room_id.split("id")
    for id in array:
        if str(my_id) != id:
            return id

# views
def index(request):
    current_user = None
    if request.user.id:
        current_user = User.objects.get(pk=request.user.id)

    # 챗방목록+챗목록 = 챗목록에서 . 필터를 한다
    chat_list = ChatList.objects.filter(
        # first_user_id가 리퀘스트 유저이거나 second_user_id가 리퀘스트 유저인 챗방을
        Q(first_user_id=request.user.id) | Q(second_user_id=request.user.id)
    # 관련된걸 불러와
    ).prefetch_related(
        Prefetch(
            # related_chat이라는걸 (models에 relate_name으로 지정해둠)
            'related_chat',
            # related_chat를 id 역순으로
            queryset=ChatLog.objects.order_by('-id'),
            # chat_log_list이라는 이름에 저장
            to_attr='chat_log_list'
        )
    )

    # 챗방목록 + 챗목록을 돌아
    for a in chat_list:
        # 챗방 목록에서 ", " 로 나눠서 돌아
        for str in a.title.split(', '):
            # 리퀘 유저 네임이랑 다른지를 확인해
            if request.user.name != str:
                # 다르면 opp_name에 이름을 박아
                a.opp_name = str
        # recent_chat_text에 챗방목록 + 챗목록에서 챗 목록중 첫번째 항목의 chat_text를 저장
        a.recent_chat_text = a.chat_log_list[0].chat_text

    context = {
        'current_user':current_user,
        'chat_list': chat_list,
    }
    return render(request, 'chat/index.html', context)

# 채팅방 입장 (index.html 에서 사용), 채팅 로그 남기기(room.html에서 사용)
def room(request, room_name):
    current_user = None
    if request.user.id:
        current_user = User.objects.get(pk=request.user.id)

    chat_list = ChatList.objects.filter(Q(first_user_id=request.user.id) | Q(second_user_id=request.user.id)).prefetch_related(Prefetch('related_chat', queryset=ChatLog.objects.order_by('-id'), to_attr='chat_log_list'))

    if request.method == "POST":
        chat_log = ChatLog()
        chat_log.chat_room_id = get_object_or_404(ChatList, chat_room_id=room_name)
        chat_log.chat_user = request.user
        chat_log.chat_text = json.loads(request.body).get('text')
        if chat_log.chat_text == '' or chat_log.chat_text == None:
            return HttpResponse(status=400)
        chat_log.save()

        return HttpResponse(status=200)
    else:
        chat_room = get_object_or_404(ChatList, chat_room_id=room_name)
        chat_log = ChatLog.objects.filter(chat_room_id=chat_room)

        for a in chat_list:
            for str in a.title.split(', '):
                if request.user.name != str:
                    a.opp_name = str
            a.recent_chat_text = a.chat_log_list[0].chat_text
        
        opp_obj = get_object_or_404(User, id=opp_id(request.user.id, room_name))

        context = {
            'current_user':current_user,
            'room_name': room_name,
            'chat_logs': chat_log, 
            'chat_list': chat_list,
            'opp_obj': opp_obj,
        }
        return render(request, 'chat/room.html', context)

# 채팅방 생성 or 채팅방 입장 (user.html, user_search.html 유저 검색 리스트에서 사용)
def create_chat_room(request, me_id, opp_id):
    # 채팅방 ID 생성
    chat_room_id = create_room_id(me_id, opp_id)

    # 채팅방이 이미 존재하는가?
    if ChatList.objects.filter(chat_room_id=chat_room_id).exists():
        # context = {
        #     'room_name': chat_room_id,
        # }
        return room(request, chat_room_id)
    
    else:
        new_chat = ChatList()
        new_chat_log = ChatList()
        if me_id < opp_id:
            new_chat.first_user_id = get_object_or_404(models.User, pk=me_id).id
            new_chat.second_user_id = get_object_or_404(models.User, pk=opp_id).id
        else:
            new_chat.second_user_id = get_object_or_404(models.User, pk=me_id).id
            new_chat.first_user_id = get_object_or_404(models.User, pk=opp_id).id

        new_chat.chat_room_id = chat_room_id
        new_chat.title = request.user.name + ", " + get_object_or_404(models.User, pk=opp_id).name
        new_chat.save()

        chat_log = ChatLog()
        chat_log.chat_room_id = get_object_or_404(ChatList, chat_room_id=chat_room_id)
        chat_log.chat_user = request.user
        chat_log.chat_text = "채팅방을 열었습니다."
        chat_log.save()

        return room(request, chat_room_id)

