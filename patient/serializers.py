from rest_framework import serializers
from patient.models import Patient
from helprequest.models import HelpRequest

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'country', 'gender']


class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        fields = [
            'patient', 'medic',
            'medic_notes', 'patient_notes',
            'patient_location', 'time_requested',
            'time_accepted', 'time_concluded'
            ]

