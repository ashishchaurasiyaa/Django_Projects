from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def thankyou(request):
    return render(request,'enroll/succes.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.clean_password())
            print('Repeat Password:', fm.clean_password())
            return HttpResponseRedirect('/regi/success/')
    else:
        fm = StudentRegistration()
        print('Ye Get Request se aya hai')

    return render(request, 'enroll/userregistration.html', {'form': fm})
