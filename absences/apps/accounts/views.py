""" apps/accounts/views.py """

from django.contrib.auth.views import LoginView

from .forms import AbsencesLoginForm


class AbsencesLoginView(LoginView):
    """ Login view. """
    form_class = AbsencesLoginForm
    template_name = 'accounts/login.html'
