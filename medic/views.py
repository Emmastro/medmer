from medic.models import Medic
from rest_framework.reverse import reverse
import jwt, datetime
from django.contrib.auth.hashers import check_password
from django.views.generic.edit import FormView
from medic.forms import MedicForm
from django.shortcuts import render, redirect



def medic_registration(request):
    form_class = MedicForm
    form  = form_class(request.POST or None)
    if request.method == 'POST':
        #form = MedicForm(request.POST, request.FILES)
        
        if form.is_valid():

             form.save()
             return redirect('home')
             
            
    context = {'form': form}
    return render(request, 'medic_registration.html', context)
