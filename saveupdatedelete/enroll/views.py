from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def thankyou(request):
    return render(request,'enroll/succes.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm,email = em,password=pw)
            reg.save()
        return HttpResponseRedirect('/regi/success/')
    else:
        fm = StudentRegistration()
        print('Ye Get Request se aya hai')
    return render(request,'enroll/userregistration.html',{'form':fm})
