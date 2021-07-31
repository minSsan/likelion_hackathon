from django.urls import path
from .views import *

app_name = 'team_build'

urlpatterns = [
    path('team_build/', RecruitListView.as_view(), name='team_build'),
    path('team_build/<str:input_role>', recruit_role_search, name='recruit_role_search'),
    
    path('create_recruit/', create_recruit, name='create_recruit'),
    path('update_recruit/<int:id>/', update_recruit, name='update_recruit'),
    path('detail_recruit/<int:id>/', detail_recruit, name='detail_recruit'),
    path('delete_recruit/<int:id>/', delete_recruit, name='delete_recruit'),
]