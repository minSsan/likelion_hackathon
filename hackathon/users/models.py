from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

from team_build.models import LOCATE_CHOICES

# User
CAREER_CHOICES = [
    ('0','1년 미만'),
    ('1','1년'),
    ('2','2년'),
    ('3','3년'),
    ('4','4년'),
    ('5','5년'),
    ('6','6년'),
    ('7','7년'),
    ('8','8년'),
    ('9','9년'),
    ('10','10년 이상'),
]

STATE_CHOICES = [
    ('','미입력'),
    ('ATTENDING','재학중'),
    ('ABSENCE','휴학중'),
    ('SEARCHING','구직중'),
    ('WORKING','재직중'),
]

ROLE_CHOICES = [
    ('Developer', '개발자'),
    ('Designer', '디자이너'),
    ('Planner', '기획자'),
    ('Etc', '그 외'),
]

# 회원 정보
class User(AbstractUser):
    name = models.CharField(default='', max_length=300)
    birth_date = models.DateField(default=timezone.now)
    address_sido = models.CharField(default='', choices=LOCATE_CHOICES, max_length=200)
    address_gungu = models.CharField(default='', max_length=200)
    career = models.CharField(default='0', max_length=200, choices=CAREER_CHOICES)
    state = models.CharField(default='', blank=True, null=False, max_length=200, choices=STATE_CHOICES)
    role = MultiSelectField(default='Etc', choices=ROLE_CHOICES, max_choices=4, max_length=200)
    intro = models.TextField(default="", blank=True, null=False)