from django.urls import path
from .views import *

app_name='scout'

urlpatterns = [
    # 유저 검색
    path('', user, name='user'),
    path('<str:input_role>', user_search, name='user_search'),
    path('search_text/<str:input_text>', user_search_text, name='user_search_text'),

    # 유저 찜
    path('user_like/<int:user_id>', user_like, name="user_like"),
]