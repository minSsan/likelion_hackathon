# chat/views.py
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

import sys, os, json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('app'))))
from app import models

# custom function
def create_room_id(num1, num2):
    if num1 < num2:
        id = num1 + "id" + num2
        return id
    else:
        id = num2 + "id" + num1
        return id

# views
def index(request):
    chat_list = models.ChatList.objects.filter(first_user_id=request.user.id)
    chat_list2 = models.ChatList.objects.filter(second_user_id=request.user.id)
    context = {
        'chat_list': chat_list,
        'chat_list2': chat_list2,
    }
    return render(request, 'chat/index.html', context)

# 채팅방 입장 (index.html 에서 사용), 채팅 로그 남기기
def room(request, room_name):
    if request.method == "POST":
        chat_log = models.ChatLog()
        chat_log.chat_room_id = get_object_or_404(models.ChatList, chat_room_id=room_name)
        chat_log.chat_text = json.loads(request.body).get('text')
        if chat_log.chat_text == '' or chat_log.chat_text == None:
            return HttpResponse(status=400)
        chat_log.save()

        return HttpResponse(status=200)
    else:
        chat_room = get_object_or_404(models.ChatList, chat_room_id=room_name)
        chat_log = models.ChatLog.objects.filter(chat_room_id=chat_room)
        context = {
            'room_name': room_name,
            'chat_logs': chat_log, 
        }
        return render(request, 'chat/room.html', context)

# 채팅방 생성 or 채팅방 입장 (user.html, user_search.html 유저 검색 리스트에서 사용)
def create_chat_room(request, me_id, opp_id):
    # 채팅방 ID 생성
    chat_room_id = create_room_id(me_id, opp_id)

    # 채팅방이 이미 존재하는가?
    if models.ChatList.objects.filter(chat_room_id=chat_room_id).exists():
        context = {
            'room_name': chat_room_id,
        }
        return render(request, 'chat/room.html', context)
    
    else:
        new_chat = models.ChatList()
        if me_id < opp_id:
            new_chat.first_user_id = get_object_or_404(models.User, pk=me_id).id
            new_chat.second_user_id = get_object_or_404(models.User, pk=opp_id).id
        else:
            new_chat.second_user_id = get_object_or_404(models.User, pk=me_id).id
            new_chat.first_user_id = get_object_or_404(models.User, pk=opp_id).id

        new_chat.chat_room_id = chat_room_id
        new_chat.title = request.user.name + ", " + get_object_or_404(models.User, pk=opp_id).name
        new_chat.save()

        chat_list = models.ChatList.objects.filter(first_user_id=request.user.id)
        chat_list2 = models.ChatList.objects.filter(second_user_id=request.user.id)
        context = {
            'chat_list': chat_list,
            'chat_list2': chat_list2,
        }
        return render(request, 'chat/index.html', context)

