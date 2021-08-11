from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# from team_build.models import LOCATE_CHOICES

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
    image = models.ImageField(default="image/users/none/profile_default.png", upload_to="image/users" , blank=True, null=False)
    name = models.CharField(default='', max_length=300)
    birth_date = models.DateField(default=timezone.now)
    address_sido = models.CharField(default='', choices=LOCATE_CHOICES, max_length=200)
    address_gungu = models.CharField(default='', max_length=200)
    career = models.CharField(default='0', max_length=200, choices=CAREER_CHOICES)
    state = models.CharField(default='', blank=True, null=False, max_length=200, choices=STATE_CHOICES)
    role = MultiSelectField(default='Etc', choices=ROLE_CHOICES, max_choices=4, max_length=200)
    intro = models.TextField(default="", blank=True, null=False)
