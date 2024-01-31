from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    return HttpResponse("<h2>This is Home Page </h2>")

def excp(request):
    print("I am Exception")
    a =10/0
    return HttpResponse("This is Excp Page")

def user_info(request):
    print("I am User Info View")
    context = {'name':'Rahul'}
    return TemplateResponse(request,'hooks/user.html',context)
