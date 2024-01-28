from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method =="POST":
        # fm = UserCreationForm(request.POST)
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully !!')
            fm.save()
    else:
        fm = SignUpForm()
        # fm = UserCreationForm()
    return render(request,'enroll/signup.html',{'form':fm})