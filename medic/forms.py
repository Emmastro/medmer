from django import forms
from medic.models import Medic

class MedicForm(forms.ModelForm):
    #password = forms.CharField(max_length=200, write_only=True)
    #wner = forms.ReadOnlyField(source='owner.username')

    class Meta:
        model = Medic
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'country', 'medic_id', 'speciality', 'password',]
        
