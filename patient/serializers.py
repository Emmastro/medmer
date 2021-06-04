from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.models import User
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'email', 'age', 'name', 'country', 'gender', 'patient']
        
class UserSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(many=True, queryset=Patient.objects.all())
owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'patient', 'owner']

      

