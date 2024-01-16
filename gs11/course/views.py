from django.shortcuts import render

# Create your views here.
def course_django(request):
    return render(request,'course/courseone.html',{'nm':'Django Course','title':'Learn Django'})
