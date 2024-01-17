from django.shortcuts import render

# Create your views here.

def course_django(request):
    return render(request,'course/courseone.html',{'name':'Django Course','title':'Django'})
