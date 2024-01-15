from django.shortcuts import render
from datetime import datetime

# Create your views here.

# def learn_django(request):
#     cname = 'Django'
#     duration = '4 Months'
#     seats = 10
#     django_details = {'nm':cname, 'du':duration, 'st':seats}
#     return render(request,'course/courseone.html',context=django_details)

def learn_django(request):
    django_details = {'nm':'Django is Awesome'}
    return render(request,'course/courseone.html',django_details)


def learn_django_time(request):
    d = datetime.now()
    return render(request,'course/coursetwo.html',{'dt':d})


def lern_django_float(request):
    return render(request,'course/coursetwo.html',{'p1':56.24321,'p2':56.00000,'p3':56.37000})

def learn_tags_python(request):
    return render(request,'course/coursethree.html',{'nm':'Django','st':5})

def learn_tags_dot_lookup(request):
    student = {'name':['Aman','Ajay','Shubham','Vishal','Viany','Atul']}
    stu= {'stu1':{'name':'Rahul','roll':101},
          'stu2': {'name': 'Aman', 'roll': 102},
          'stu3': {'name': 'Ajay', 'roll': 103},
          'stu4': {'name': 'Vinay', 'roll': 104},
          }
    students = {'student':stu}
    return render(request,'course/coursefour.html',students)

def learn_loop_tags(request):
    data = {'name':'Rahul','roll':101}
    return render(request,'course/coursefive.html',{'dt':data})