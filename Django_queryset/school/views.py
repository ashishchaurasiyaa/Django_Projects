from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
# Create your views here.

def home(request):
    student_data=Student.objects.all()
    # student_data=Student.objects.filter(marks = 70)
    # student_data=Student.objects.exclude(marks=70)
    # student_data=Student.objects.order_by('name')
    # student_data=Student.objects.order_by('-name')
    # student_data=Student.objects.order_by('?')
    # student_data=Student.objects.order_by('id').reverse()[:2]
    # student_data=Student.objects.values('name','city')
    # student_data=Student.objects.values_list(named=True)
    # student_data=Student.objects.values_list('id','name',named=True)
    # student_data=Student.objects.using('default')
    # student_data=Student.objects.dates('pass_date','day')

    # Second table
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)
    # student_data = qs1.union(qs2) #union combine two table data and both choose same number of columns
    # student_data = qs1.union(qs2,all=True)
    # student_data = qs1.intersection(qs2)
    # student_data = qs1.difference(qs2)

    # Operator AND
    # student_data = Student.objects.filter(id = 3) & Student.objects.filter(city='Delhi')
    # student_data = Teacher.objects.filter(id = 3) | Teacher.objects.filter(city='Kanpur')
    # student_data = Teacher.objects.filter(Q(id=3) & Q(city='Delhi'))
    # student_data = Teacher.objects.filter(Q(id=3) | Q(city='Delhi'))


    # student_data = Student.objects.filter(name__contains='a')

    # # QuerySet API Methods that do not return new QuerySets in Django
    # # Get method
    # student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.get(pk=1)
    # # first() method
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.last()
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')
    # student_data = Student.objects.all()
    # print(student_data.exists())
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())
    # student_data = Student.objects.create(name='Vinod',roll=105,city='Bokaro',marks=65,pass_date='2024-01-10')
    # student_data,created = Student.objects.get_or_create(name='Abhishek',roll=106,city='Bokaro',marks=65,pass_date='2024-01-10')

    # student_data = Student.objects.filter(id=12).update(name='Rahul',marks=80)
    # student_data = Student.objects.filter(id=12).filter(marks=70).update(city='Pass')

    # student_data=Student.objects.update_or_create(id=2,name='Ajay',defaults={'name':'Virat'})

    # objs = [
    #     Student(name='Rahul',roll=101,city='Ranchi',marks=70,pass_date='2024-01-10'),
    #     Student(name='Karan',roll=102,city='Ranchi',marks=70,pass_date='2024-02-01'),
    #     Student(name='Abhishek',roll=103,city='Delhi',marks=70,pass_date='2024-01-10'),
    # ]
    # student_data= Student.objects.bulk_create(objs)
    # all_student_data =Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Dhanbad'
    # student_data = Student.objects.bulk_update(all_student_data,['city'])
    # student_data=Student.objects.in_bulk([1,2])
    # student_data=Student.objects.in_bulk([])
    # student_data=Student.objects.in_bulk()
    # # print(student_data[1].name)
    # student_data=Student.objects.get(pk=2).delete()
    # student_data=Student.objects.filter(marks=65).delete()
    # student_data=Student.objects.all().delete()
    # student_data=Student.objects.all()



    # print(student_data.count())



    # print("SQL Query",student_data.query)
    return render(request,'school/home.html',{'students':student_data})

