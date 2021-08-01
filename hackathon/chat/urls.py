# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('in/<str:me_id>/<str:opp_id>/', views.create_chat_room, name='create_chat_room'),
]