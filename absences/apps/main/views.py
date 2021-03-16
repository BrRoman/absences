""" apps/main/views.py """

from django.shortcuts import render


def home(request):
    """ Home view of absences. """
    return render(request, 'main/home.html')
