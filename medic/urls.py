from django.urls import path 
#from django.views.generic import 
from medic import views

urlpatterns = [


path('', views.MedicRegistration.as_view(), name='medic_registration')
 ]