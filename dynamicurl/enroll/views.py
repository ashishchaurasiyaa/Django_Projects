from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'enroll/home.html')
def dynamic(request,my_id):
    if my_id == 1:
        student = {'id':my_id,'name':'Ashish'}
    if my_id == 2:
        student = {'id':my_id,'name':'Shubham'}
    if my_id == 3:
        student = {'id':my_id,'name':'Vinay'}
    if my_id == 4:
        student = {'id':my_id,'name':'Atul'}
    return render(request,'enroll/dynamic.html',student)

def show_subdetails(request,my_id,my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id':my_id,'name':'Ashish','info':'Sub Details'}

    if my_id == 2 and my_subid == 6:
        student = {'id':my_id, 'name':'Shubham','info':'Sub Details'}

    if my_id == 3 and my_subid == 7:
        student = {'id':my_id, 'name':'Ankit','info':'Sub Details'}

    return render(request,'enroll/dynamic.html',student)
