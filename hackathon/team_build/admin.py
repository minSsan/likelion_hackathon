from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Recruit),
admin.site.register(Comment),
admin.site.register(CommentAnswer),
admin.site.register(LikeRecruit),