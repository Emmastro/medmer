from rest_framework import serializers
from medic.models import Medic


class MedicSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Medic
        fields = ['email', 'name', 'country', 'medic_id', 'speciality']
