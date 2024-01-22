from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm =StudentRegistration(auto_id=True, label_suffix=' ',initial={'name':'Ashish Chaurasiya','email':'ashishkumar.mailto@gmail.com','first_name':'Ashish','last_name':'Chaurasiya'})
    fm.order_fields(field_order=['email','first_name','last_name'])
    return render(request,'enroll/userregistration.html',{'form':fm,'title':'Form'})
