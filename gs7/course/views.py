from django.http import HttpResponse

def coursedj(request):
    return HttpResponse('Course Django')

def coursePython(request):
    return HttpResponse('Course Python')