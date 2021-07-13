from django import forms
from django.contrib.auth.forms import UserCreationForm
from helprequest.models import HelpRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class HelpRequestForm(forms.ModelForm):

    class Meta:
        model = HelpRequest
        fields = ['patient_notes', 'patient_location']
        optional_fields = ['patient']

class HelpResponseForm(forms.ModelForm):
    """
    form for medic when they accept and attend to a patient
    """

    class Meta:
        model = HelpRequest
        fields = ['medic_notes']
        
