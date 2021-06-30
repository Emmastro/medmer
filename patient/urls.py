from django.urls import path 
#from django.views.generic import 
from patient import views

urlpatterns = [


path('', views.patientRegistration, name='Patient_Reg'),
 ]