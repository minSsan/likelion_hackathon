from django.db import models
from django.db.models.deletion import CASCADE

from users.models import User

class LikeUser(models.Model):
    # 어떤 유저의 찜 정보인지
    user = models.CharField(default="", max_length=200)
    # 어떤 유저를 찜했는지 해당 유저 정보를 저장
    # 해당 유저가 지워지면 찜 내역도 사라짐
    user_key = models.ForeignKey(User, on_delete=CASCADE)