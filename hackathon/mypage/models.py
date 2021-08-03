from django.db import models
from django.db.models.deletion import CASCADE

from users.models import User
from team_build.models import Recruit

class LikeRecruit(models.Model):
    # 어떤 유저의 찜 정보인지 user id를 저장(request.user 값이 들어갈 것임)
    user = models.CharField(default="", max_length=200)
    # 해당 유저가 어떤 모집글을 찜했는지 해당 모집글의 id를 저장
    recruit_key = models.ForeignKey(Recruit, on_delete=CASCADE)
