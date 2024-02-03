from django.shortcuts import render
from .models import Student, ProxyStudent

# Create your views here.

def home(request):
    # students = Student.objects.all()
    # students = Student.students.get_stu_roll_range(101,104)
    # students = ProxyStudent.students.get_stu_roll_range(101,104)
    students = ProxyStudent.students.all()
    # students = Student.students.all()
    print(students)
    return render(request, 'school/home.html', {'students':students})
