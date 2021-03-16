""" absences/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('absences/', include('apps.main.urls')),
    path('absences/accounts/', include('apps.accounts.urls')),
    path('absences/admin/', admin.site.urls),
]
