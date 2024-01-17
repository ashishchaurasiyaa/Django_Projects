from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'core/base.html',{'title':'Base'})
def home(request):
    return render(request,'core/home.html',{'title':'Home'})

def about(request):
    return render(request,'core/about.html',{'title':'about'})
