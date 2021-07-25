from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

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
    ('SEARCHING','구직중'),
    ('OFFERING','구인중'),
    ('WORKING','재직중'),
]

ROLE_CHOICES = [
    ('Developer', '개발자'),
    ('Designer', '디자이너'),
    ('Planner', '기획자'),
    ('Etc', '그 외'),
]

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
    ('Etc', '그 외'),
]
    
# 회원 정보
class User(AbstractUser):
    name = models.CharField(default='', max_length=300)
    birth_date = models.DateField(default=timezone.now)
    address_sido = models.CharField(default='', max_length=100)
    address_gungu = models.CharField(default='', max_length=100)
    career = models.CharField(default='0', max_length=2, choices=CAREER_CHOICES)
    state = models.CharField(default='', max_length=9, choices=STATE_CHOICES)
    role = MultiSelectField(default='Etc', choices=ROLE_CHOICES, max_choices=4, max_length=9)
    want = models.CharField(default='', max_length=500)

# 포트폴리오
class Portfolio(models.Model):
    title = models.CharField(default='', max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # ForiegnKey(외래키): 외부 테이블 키를 가져옴.
    # 여기서는 User(부모 테이블)라는 테이블의 키를 Portfolio(자식 테이블)에 받아옴
    detail = models.TextField(blank=True, null=True)
    # 추후 변경 => 네이버 스마트 에디터 활용방안 고안
    # 프론트에서 네이버 에디터에 작성된 내용이 전달되는 형태가
    # 어떻게 되는지에 따라 필드를 달리 설정할 가능성 있음

# 팀원 모집 글
class Recruit(models.Model):
    title = models.CharField(default='', max_length=300) # 프로젝트 한줄 설명으로 들어갈 것
    team_name = models.CharField(default='', max_length=200)
    service = models.CharField(default='', max_length=100)
    team_members = models.CharField(
        default='1',
        blank=True,
        null=False,
        max_length=1,
        choices=TEAM_MEMBERS_CHOICES
        )
    service_level = models.CharField(
        default='0',
        null=False,
        blank=True,
        max_length=1,
        choices=LEVEL_CHOICES
        )
    founding_date = models.DateField(default=timezone.now, null=False, blank=True)
    locate = models.CharField(default='', max_length=2,choices=LOCATE_CHOICES)
    image = models.ImageField(default='', blank=True, null=False)
    # 추후 기본 이미지로 넣을 경로 찾아서 default 에 지정 필요
    role = MultiSelectField(default='Etc', choices=ROLE_CHOICES, max_choices=4, max_length=9)
    # role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    detail = models.TextField(blank=True, null=True)