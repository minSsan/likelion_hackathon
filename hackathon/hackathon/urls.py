"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', main, name="main"),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/<int:id>', profile, name='profile'),

    path('create_recruit/', create_recruit, name='create_recruit'),
    path('update_recruit/<int:id>/', update_recruit, name='update'),
    path('detail_recruit/<int:id>/', detail_recruit, name='detail_recruit'),
    path('delete_recruit/<int:id>/', delete_recruit, name='delete_recruit'),
    
    path('profile/<int:user_id>/create_pf/', create_portfolio, name="create_pf"),
    path('profile/<int:user_id>/detail_pf/<int:pf_id>/', detail_portfolio, name='detail_pf'),
    path('profile/<int:user_id>/detail_pf/update/<int:pf_id>/', update_portfolio, name="update_pf"),
    path('profile/<int:user_id>/detail_pf/delete/<int:pf_id>/', delete_portfolio, name='delete_pf'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)