from django.urls import path
from medic import views

urlpatterns = [
  path(' ', views.MedicList),
  path('<int:pk>/', views.MedicDetail),
]