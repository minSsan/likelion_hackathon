from django.db import models

class ChatList(models.Model):
    title = models.CharField(max_length=200)
    first_user_id = models.CharField(max_length=300)
    second_user_id = models.CharField(max_length=300)
    chat_room_id = models.CharField(max_length=400)

class ChatLog(models.Model):
    chat_room_id = models.ForeignKey(ChatList, on_delete=models.CASCADE, null=True)
    chat_text = models.TextField()