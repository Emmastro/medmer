from django.urls import path 
#from django.views.generic import 
from medic import views

urlpatterns = [


path('', views.MedicRegistration, name='Medic_Reg')
 ]