from django import forms
from django.contrib.auth.forms import UserCreationForm
from helprequest.models import HelpRequest



class HelpRequestForm(forms.ModelForm):
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
        
