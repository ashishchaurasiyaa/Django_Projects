from django.shortcuts import render

# Create your views here.
# def setsession(request):
#     # request.session['name'] = 'Ashish'
#     request.session['name'] = 'Ashish'
#     request.session['lname'] = 'Chaurasiya'
#     return render(request, 'session/setsession.html')
#
# def getsession(request):
#     # name = request.session['name']
#     name = request.session.get('name')
#     keys = request.session.keys()
#     items = request.session.items()
#     # age = request.session.setdefault('age','26')
#
#     return render(request,'session/getsession.html',{'name':name,'keys':keys,'items':items})
#
# # def delsession(request):
# #     if 'name' in request.session:
# #         del request.session['name']
# #     return render(request,'session/delseesion.html')
# def delsession(request):
#     request.session.flush()
#     return render(request,'session/delseesion.html')
def setsession(request):
    request.session['name'] = 'Ashish'
    request.session.set_expiry(600)
    return render(request, 'session/setsession.html')

def getsession(request):
    name = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request,'session/getsession.html',{'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'session/delseesion.html')