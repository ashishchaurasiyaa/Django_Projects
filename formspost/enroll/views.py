from django.shortcuts import render,HttpResponseRedirect

from .forms import StudentRegistration

# Create your views here.

def thankyou(request):
    return render(request,'enroll/succes.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name',name)
            print('Email', email)
            print('Password',password)
            return HttpResponseRedirect('/regi/success/')
            # return render(request,'enroll/succes.html',{'nm':name})
    else:
        fm = StudentRegistration()
        print('Ye Get Request se aya hai')
    return render(request,'enroll/userregistration.html',{'form':fm})
