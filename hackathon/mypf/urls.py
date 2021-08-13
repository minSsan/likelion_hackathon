from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mypf'

urlpatterns = [
    path('<int:id>', profile, name='profile'),
    path('<int:user_id>/create_pf/', create_portfolio, name="create_pf"),
    path('<int:user_id>/<int:pf_id>/', detail_portfolio, name='detail_pf'),
    path('<int:user_id>/update/<int:pf_id>/', update_portfolio, name="update_pf"),
    path('<int:user_id>/delete/<int:pf_id>/', delete_portfolio, name='delete_pf'),
]