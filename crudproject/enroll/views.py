from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import StudentRegitration
from .models import User


# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegitration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegitration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=id)
        user.delete()
    return HttpResponseRedirect('/')


def update_data(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        fm = StudentRegitration(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegitration(instance=user)
    return render(request, 'enroll/updatestudent.html', {'form': fm})
