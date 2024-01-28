from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def setcookie(request):
    reponse = render(request,'cookies/setcookie.html')
    # reponse.set_cookie('name','sonam',max_age=60)
    reponse.set_cookie('fname','Ashish',expires=datetime.utcnow()+timedelta(days=2))
    return reponse


def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name',"Guest")
    return render(request,'cookies/getcookie.html',{'name':name})

def delcookie(request):
    reponse = render(request,'cookies/delcookie.html')
    reponse.delete_cookie('name')
    return reponse
