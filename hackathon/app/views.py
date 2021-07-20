from django.shortcuts import render
from .models import *

def main(request):
    recruit_posts = Recruit.objects.all()
    context = {
        'posts':recruit_posts,
    }
    return render(request, 'main.html', context)