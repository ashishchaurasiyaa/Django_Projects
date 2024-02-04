from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.
class MyView(View):
    name = 'Ashish'
    def get(self, request):
        return HttpResponse(self.name)

class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)

class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html',{'title':'Class Based'})

class AboutClassView(View):
    def get(self, request):
        return render(request, 'school/about.html',{'title':'Class Based About Us'})

class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html',{'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse ('Form Submitted Successfully')

