from rest_framework import serializers
from .models import HelpRequest


class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        fields = [
            'patient', 'medic',
            'medic_notes', 'patient_notes',
            'patient_location', 'time_requested',
            'time_accepted', 'time_concluded'
            ]
