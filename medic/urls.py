from django.urls import path 
#from django.views.generic import 
from medic import views

urlpatterns = [

#path('', views.MedicList.as_view()),
#path('<int:pk>/', views.MedicDetail.as_view()),
path('', views.register, name='register')
#path('login', views.LoginView.as_view()),
#path('user', views.Userview.as_view()),
 ]