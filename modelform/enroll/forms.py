from django import forms
from django.core import validators
from .models import User
class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))


    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name', 'password':'Enter Password','email':'Enter Email'}
        # error_messages = {
        #     'name':{'required':'Name is compulsory'},
        #     'password':{'required':'Password is compulsory'}
        # }
        widgets = {
            'password':forms.PasswordInput
            # 'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Name'})
        }