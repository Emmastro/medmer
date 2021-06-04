from django.urls import path
from medic import views

urlpatterns = [
    path('medic/', views.medic_list),
    path('medic/<int:pk>/', views.medic_detail),
]