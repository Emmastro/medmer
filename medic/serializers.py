from rest_framework import serializers
from medic.models import Medic

class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = ['id', 'email', 'medic_id', 'name', 'country']
        