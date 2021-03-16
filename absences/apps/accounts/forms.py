""" apps/accounts/forms.py """

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AbsencesLoginForm(AuthenticationForm):
    """ Login form of Absences. """
    username = forms.CharField(
        label='Utilisateur :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        widget=forms.EmailInput(
            attrs={'autofocus': True}
        ),
    )
    password = forms.CharField(
        label='Entrez votre mot de passe :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password'}
        ),
    )

    error_messages = {
        'invalid_login': 'Données non valides',
    }
