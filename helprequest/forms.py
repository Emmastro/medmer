from django import forms
from django.contrib.auth.forms import UserCreationForm
from helprequest.models import HelpRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout




class HelpRequestForm(forms.ModelForm):
    patient_notes = forms.TextInput()
    patient_location = forms.TextInput()
    
    class Meta:
        model = HelpRequest
        fields = ['patient_notes', 'patient_location',]
        exclude = ['medic-notes ']

class HelpResponseForm(forms.ModelForm):
    """
    form for medic when they accept and attend to a patient
    """

    class Meta:
        model = HelpRequest
        fields = ['medic_notes']
        
