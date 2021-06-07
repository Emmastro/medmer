from django.urls import path
from medic import views

urlpatterns = [
  path('', views.MedicList.as_view()),
  path('<int:pk>/', views.MedicDetail.as_view()),
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>/', views.UserDetail.as_view()),
]