from django.shortcuts import render

###### 메인 페이지 ######
def main(request):
    return render(request, 'main/main.html')
