from django.shortcuts import render

from users.models import User

###### 메인 페이지 ######
def main(request):
    user_instance = None
    if request.user.id:
        user_instance = User.objects.get(pk=request.user.id)
    return render(request, 'main/main.html', {'user_instance':user_instance})
