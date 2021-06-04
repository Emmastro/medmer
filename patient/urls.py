from django.urls import path
from patient import views

urlpatterns = [
    path('patient/', views.medic_list),
    path('patient/<int:pk>/', views.patient_detail),
]