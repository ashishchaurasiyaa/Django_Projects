from django.shortcuts import render,request

# Create your views here.

def chatPage(request):
    return render(request,"chat/chat.html")
