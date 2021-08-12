# chat/urls.py
from django.urls import path

from .views import *

app_name = 'chat'

urlpatterns = [
    path('index/', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    path('<str:me_id>/<str:opp_id>/', create_chat_room, name='create_chat_room'),
]