from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=5, max_length=50, strip=False, empty_value='Ashish', error_messages={'required':'Enter Your Name'})
    # email = forms.EmailField(min_length=5,max_length=50)
    # # password = forms.CharField(min_length=5,max_length=50,widget=forms.PasswordInput)
    #
    # # validation
    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_name = self.cleaned_data['name']
    #     val_email = self.cleaned_data['email']
    #     if len(val_name) < 4:
    #         raise forms.ValidationError('Name should be more than 4 or equal')
    #     if len(val_email)<10:
    #         raise forms.ValidationError('Email should be grater than 10 characters')
    #
    #
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField()


