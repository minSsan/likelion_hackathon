from django.urls import path
from .views import *

app_name = 'team_build'

urlpatterns = [
    # 모집글 검색
    path('team_build/', RecruitListView.as_view(), name='team_build'),
    path('team_build/<str:input_role>', recruit_role_search, name='recruit_role_search'),
    
    # 모집글
    path('create_recruit/', create_recruit, name='create_recruit'),
    path('update_recruit/<int:id>/', update_recruit, name='update_recruit'),
    path('detail_recruit/<int:id>/', detail_recruit, name='detail_recruit'),
    path('delete_recruit/<int:id>/', delete_recruit, name='delete_recruit'),

    # 댓글
    path('detail_recruit/<int:id>/create_comment/', create_comment, name='create_comment'),
    path('detail_recruit/<int:id>/delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
    path('detail_recruit/<int:id>/update_comment/<int:comment_id>', update_comment, name='update_comment'),
]