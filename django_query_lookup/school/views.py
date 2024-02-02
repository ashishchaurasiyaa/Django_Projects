from django.shortcuts import render
from .models import Student
from datetime import date,time
from django.db.models import Avg, Sum,Max,Min,Count
from django.db.models import Q

# Create your views here.

def home(request):
    # student_data= Student.objects.all()
    # student_data= Student.objects.filter(name__exact='Ashish')
    # student_data= Student.objects.filter(name__iexact='ashish')
    # student_data= Student.objects.filter(name__contains='a')
    # student_data= Student.objects.filter(name__icontains='A')
    # student_data= Student.objects.filter(id__in=[1,2])
    # student_data= Student.objects.filter(marks__in=[80])
    # student_data= Student.objects.filter(marks__gt=80)
    # student_data= Student.objects.filter(marks__gte=80)
    # student_data= Student.objects.filter(marks__lt=80)
    # student_data= Student.objects.filter(marks__lte=80)
    # student_data= Student.objects.filter(name__startswith='a')
    # student_data= Student.objects.filter(name__endswith='m')
    # student_data= Student.objects.filter(name__endswith='m')
    # student_data= Student.objects.filter(passing_year__range=('2021-01-01','2021-12-31'))
    # student_data=Student.objects.filter(admissoon_date__date=date(2021,7,1))
    # student_data=Student.objects.filter(admissoon_date__date__gt=date(2021,8,15))
    # student_data=Student.objects.filter(passing_year__year=2021)
    # student_data=Student.objects.filter(passing_year__year__gte=2021)
    # student_data=Student.objects.filter(passing_year__month__gt=7)
    # student_data=Student.objects.filter(passing_year__day=10)
    # student_data=Student.objects.filter(passing_year__week_day=15)
    # student_data=Student.objects.filter(passing_year__week=15)
    # student_data=Student.objects.filter(passing_year__quarter=3)
    # student_data=Student.objects.filter(admissoon_date__time__gt=time(18,00))
    # student_data=Student.objects.filter(admissoon_date__hour__gt=18)
    # student_data=Student.objects.filter(admissoon_date__second__gt=10)
    # student_data=Student.objects.filter(roll__isnull=False)

    # Aggregatoin
    # student_data=Student.objects.all()
    # average=student_data.aggregate(Avg('marks'))
    # sum=student_data.aggregate(Sum('marks'))
    # min=student_data.aggregate(Min('marks'))
    # max=student_data.aggregate(Max('marks'))
    # count=student_data.aggregate(Count('marks'))
    # context={'students':student_data,'average':average,'sum':sum,'min':min,'max':max,'count':count}

    # Q model
    # student_data=Student.objects.filter(Q(id='3') | Q(roll='103'))
    # student_data=Student.objects.filter(Q(id='3') & Q(roll='103'))
    # student_data=Student.objects.filter(~Q(id='3'))
    # student_data=Student.objects.all()[:5]
    # student_data=Student.objects.all()[1:3]
    student_data=Student.objects.all()[:11:3]
    print("Return:",student_data)
    # print("SQL Query:",student_data.query)

    # return render(request, 'school/home.html',{'students':student_data,'average':average,'sum':sum,'min':min,'max':max,'count':count})
    return render(request, 'school/home.html',{'students':student_data})
