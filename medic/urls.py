from django.urls import path 
#from django.views.generic import 
from medic import views

urlpatterns = [


path('', views.medicRegistration, name='Medic_Reg')
 ]