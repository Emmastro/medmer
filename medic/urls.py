from django.urls import path
from medic import views

urlpatterns = [
  path('', views.MedicList.as_view()),
  path('<int:pk>/', views.MedicDetail.as_view()),
]