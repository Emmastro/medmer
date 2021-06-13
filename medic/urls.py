from django.urls import path
from medic import views

urlpatterns = [
  #path('', views.api_root),
  path('', views.MedicList.as_view()),
  path('<int:pk>/', views.MedicDetail.as_view()),
  #path('', views.RegisterView.as_view()),
]