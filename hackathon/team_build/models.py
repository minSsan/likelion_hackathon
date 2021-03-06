from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('users'))))
from users.models import *

from django.db.models.deletion import CASCADE



# Recruit
TEAM_MEMBERS_CHOICES = [
    ('1','1명'),
    ('2','2명'),
    ('3','3명'),
    ('4','4명'),
    ('5','5명 이상'),
]

LEVEL_CHOICES = [
    ('0', '아이디어 구상 단계'),
    ('1', '초기 개발 단계'),
    ('2', '프로토타입 완성 단계'),
    ('3', '배포 및 상용화 단계'),
    ('4', '서비스 확장 단계'),
]

LOCATE_CHOICES = [
    ('','미정'),
    ('서울','서울특별시'),
    ('부산','부산광역시'),
    ('인천','인천광역시'),
    ('대구','대구광역시'),
    ('광주','광주광역시'),
    ('대전','대전광역시'),
    ('울산','울산광역시'),
    ('세종','세종시'),
    ('경기','경기도'),
    ('강원','강원도'),
    ('충남','충청남도'),
    ('충북','충청북도'),
    ('경북','경상북도'),
    ('경남','경상남도'),
    ('전북','전라북도'),
    ('전남','전라남도'),
    ('제주','제주도'),
]

ROLE_CHOICES = [
    ('Developer', '개발자'),
    ('Designer', '디자이너'),
    ('Planner', '기획자'),
    ('Editor', '편집자'),
]
# 팀원 모집 글
class Recruit(models.Model):
    # user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    writer = models.CharField(default='', max_length=200)
    writer_username = models.CharField(default='', max_length=200)
    title = models.CharField(default='', max_length=300) # 프로젝트 한줄 설명으로 들어갈 것
    team_name = models.CharField(default='', max_length=200)
    service = models.CharField(default='', max_length=200)
    team_members = models.CharField(
        default='1',
        blank=True,
        null=False,
        max_length=200,
        choices=TEAM_MEMBERS_CHOICES
        )
    service_level = models.CharField(
        default='0',
        null=False,
        blank=True,
        max_length=200,
        choices=LEVEL_CHOICES
        )
    founding_date = models.DateField(default=timezone.now, null=False, blank=True)
    locate = models.CharField(default='', null=False, blank=True, max_length=2, choices=LOCATE_CHOICES)
    image = models.ImageField(
        default='image/team_build/none/img_default.png',
        upload_to="image/team_build/",
        blank=True,
        null=False
        )
    # 추후 기본 이미지로 넣을 경로 찾아서 default 에 지정 필요
    role = MultiSelectField(default='', choices=ROLE_CHOICES, max_choices=4, max_length=100)
    # role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    detail = models.TextField(blank=True, null=True)

class Comment(models.Model):
    recruit_id = models.ForeignKey(Recruit, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=200)

class CommentAnswer(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=200)

class LikeRecruit(models.Model):
    # 어떤 유저의 찜 정보인지 user id를 저장(request.user 값이 들어갈 것임)
    user = models.CharField(default="", max_length=200)
    # 해당 유저가 어떤 모집글을 찜했는지 해당 모집글의 id를 저장
    recruit_key = models.ForeignKey(Recruit, on_delete=CASCADE)

