from django.http import HttpResponse

def feesdj(request):
    return HttpResponse('200 response error')

def feesPython(request):
    return HttpResponse('300 Server error')