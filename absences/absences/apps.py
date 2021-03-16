""" absences/apps.py """

from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    """
    New app admin. Don't forget to replace
        'django.contrib.admin',
    by
        'absences.apps.MyAdminConfig',
    in your settings.py
    """
    default_site = 'absences.admin.MyAdminSite'
