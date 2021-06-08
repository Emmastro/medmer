from django.urls import path
from helprequest import views

urlpatterns = [
    path('', views.HelpRequestList.as_view()),
    path('<int:patient_id>', views.PatientHelpRequestList.as_view()),    
    path('<int:medici_d>', views.MedicHelpRequestList.as_view()),
    path('<int:pk>/', views.HelpRequestDetail.as_view()),
]
