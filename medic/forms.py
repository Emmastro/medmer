from django import forms
from medic.models import Medic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class MedicForm(forms.ModelForm):
    class Meta:
       model = Medic
       fields = ['id', 'username', 'first_name', 'last_name', 'email', 'country', 'medic_id', 'speciality', 'password',]
        
