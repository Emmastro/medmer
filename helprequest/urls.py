from django.urls import path
from helprequest import views

urlpatterns = [
    path('', views.HelpRequestList.as_view(), name='help_requests'),
    path('<int:pk>/', views.HelpRequestDetail.as_view(), name='help_request_detail'),
    path ('requesthelp/', views.RequestHelp.as_view(), name='request_help'),
    path ('requesthelp/status', views.HelpRequestStatus.as_view(), name='request_help_status'),
]
