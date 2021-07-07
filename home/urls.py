from django.urls import path
from . import views

from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView, PasswordResetDoneView, LogoutView, \
        PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('accounts/profile/', views.profile, name='profile'),
	path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]