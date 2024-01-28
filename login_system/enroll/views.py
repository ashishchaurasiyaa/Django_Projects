from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
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
    return render(request,'enroll/signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()

        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile Updated !!!')
                return HttpResponseRedirect(reverse('profile'))
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'name': request.user.username, 'form': fm, 'users':users})
    else:
        messages.warning(request, 'Please log in to access your profile.')
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            fm = PasswordChangeForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, request.user)
                messages.info(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
            return render(request,'enroll/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_details(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request,'enroll/userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')

