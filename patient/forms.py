from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms
from patient.models import Patient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PatientForm(forms.ModelForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label= 'Email')
    country = forms.CharField()
    gender = forms.ChoiceField(choices=[('Male', 'male'), ('Female', 'female')])
    age = forms.IntegerField(max_value=100)
    
    
    class Meta:
       model = Patient
       fields = ('id', 'username', 'first_name', 
       'last_name', 'email', 'country', 
       'gender', 'age',  'password')



        
