from patient.models import Patient
from rest_framework.reverse import reverse
import jwt, datetime
from django.contrib.auth.hashers import check_password
from django.views.generic.edit import FormView
from patient.forms import PatientForm
from django.shortcuts import render, redirect



def PatientRegistration(request):
    form_class = PatientForm
    form  = form_class(request.POST or None)
    if request.method == 'POST':
        #form = PaitehtForm(request.POST, request.FILES)
        
        if form.is_valid():

             form.save()
             redirect('home')
             
            
    context = {'form': form}
    return render(request, 'patient_registration.html', context)
    