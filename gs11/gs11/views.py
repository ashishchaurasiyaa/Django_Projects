from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'home':'This is Home Page'})