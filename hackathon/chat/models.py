from django.db import models

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('users'))))
from users.models import *

class ChatList(models.Model):
    title = models.CharField(max_length=200)
    first_user_id = models.CharField(max_length=300)
    second_user_id = models.CharField(max_length=300)
    chat_room_id = models.CharField(max_length=400)
    opp_name = models.CharField(max_length=200, default='')

class ChatLog(models.Model):
    chat_room_id = models.ForeignKey(ChatList, on_delete=models.CASCADE, null=True, related_name='related_chat')
    chat_user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_text = models.TextField()
