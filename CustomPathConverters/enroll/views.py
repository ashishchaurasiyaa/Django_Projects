from django.shortcuts import render


# Create your views here.
def dynamic(request,year):
    student= {'yr':year}
    return render(request,'enroll/dynamic.html',student)
