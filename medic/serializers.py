from rest_framework import serializers
from medic.models import Medic
from django.contrib.auth.models import User
class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = ['id', 'email', 'name', 'country', 'medic_id', 'medic']
        
class UserSerializer(serializers.ModelSerializer):
    medic = serializers.PrimaryKeyRelatedField(many=True, queryset=Patient.objects.all())
owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'medic', 'owner']

