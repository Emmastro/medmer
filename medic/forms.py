from django import forms
from medic.models import Medic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MedicRegistrationForm(UserCreationForm):

    class Meta:
       model = Medic
       fields = ['id', 'username', 'first_name', 'last_name', 'email', 'country', 'medic_id', 'speciality', 'password1', 'password2']
