from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medic/', include('medic.urls')),
    path('patient/', include('patient.urls')),
    path('help-request/', include('helprequest.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
