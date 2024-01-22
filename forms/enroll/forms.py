from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1','id':'uniqueid'}))
    first_name = forms.CharField()
    last_name = forms.CharField(label='Last Name', label_suffix=' ',initial='Chaurasiya', required=False, disabled=True,help_text= 'Limit 70 Char')
    email = forms.EmailField()
    key = forms.CharField(widget=forms.HiddenInput())
