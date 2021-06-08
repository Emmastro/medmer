from django.urls import path
from patient import views

urlpatterns = [
  path('', views.PatientList.as_view()),
  path('<int:pk>/', views.PatientDetail.as_view()),
]
