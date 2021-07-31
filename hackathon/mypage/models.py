from django.db import models
from users.models import User

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
