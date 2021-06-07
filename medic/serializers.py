from rest_framework import serializers
from medic.models import Medic


class MedicSerializer(serializers.ModelSerializer):
    """ """
    password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = Medic
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'country', 'medic_id', 'speciality', 'password']
