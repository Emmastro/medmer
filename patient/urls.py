from django.urls import path
from patient import views

urlpatterns = [
  path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),

]
