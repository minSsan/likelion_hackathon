from django.urls import path
from .views import *

app_name='scout'

urlpatterns = [
    # 유저 검색
    path('', user, name='user'),
    path('search/<str:input_role>', user_search, name='user_search'),
    path('search/text/<str:input_text>', user_search_text, name='user_search_text'),
]