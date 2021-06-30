from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms
from patient.models import Patient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PatientForm(forms.ModelForm):
    class Meta:
       model = Patient
       fields = ('id', 'username', 'first_name', 
       'last_name', 'email', 'country', 
       'gender', 'age',  'password')



        
