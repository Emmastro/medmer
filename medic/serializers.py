from rest_framework import serializers
from medic.models import Medic


class MedicSerializer(serializers.ModelSerializer):
    """
    owners => allows us to associate instances with the users that created them
     """
    password = serializers.CharField(max_length=200, write_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Medic
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'country', 'medic_id', 'speciality', 'password', 'owner']
