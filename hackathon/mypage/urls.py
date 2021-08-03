from django.urls import path
from .views import *

app_name = 'mypage'

urlpatterns = [
    path('<int:user_id>', mypage, name="mypage"),
]