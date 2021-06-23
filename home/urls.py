from django.urls import path
from . import views

from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView, PasswordResetDoneView, LogoutView, \
        PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
	path('', views.home, name='home'),
	path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
	path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset' ),
	path('password_reset/done/',  PasswordResetDoneView.as_view(template_name='registration/password_reset_success.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_set.html'), name='password_reset_confirm'),
	path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_completed.html'), name='password_reset_complete'),
	path('accounts/profile/', views.profile, name='profile'),
	
]