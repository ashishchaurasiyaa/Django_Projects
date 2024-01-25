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
            print('Name:',fm.cleaned_data['name'])
            print('Email',fm.cleaned_data['email'])
            print('Password',fm.cleaned_data['password'])
            # print('Roll:',fm.cleaned_data['roll'])
            # print('Price',fm.cleaned_data['price'])
            # print('Rate',fm.cleaned_data['rate'])
            # print('Comments',fm.cleaned_data['comment'])
            # print('Website',fm.cleaned_data['website'])
            # print('Description',fm.cleaned_data['description'])
            # print('Feedback',fm.cleaned_data['feedback'])
            # print('Notes',fm.cleaned_data['notes'])
            # print('Agree',fm.cleaned_data['agree'])
        return HttpResponseRedirect('/regi/success/')
    else:
        fm = StudentRegistration()
        print('Ye Get Request se aya hai')
    return render(request,'enroll/userregistration.html',{'form':fm})
