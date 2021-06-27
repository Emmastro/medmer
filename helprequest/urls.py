from django.urls import path
from helprequest import views

urlpatterns = [
    path('', views.HelpRequestList.as_view()),
    path('<int:pk>/', views.HelpRequestDetail.as_view(), name='help_request_detail'),
   # path ('', views.PatientHelp, name='Helpinfo'),
]
