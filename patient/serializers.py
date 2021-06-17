from rest_framework import serializers
from patient.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    """
    owners => allows us to associate instances with the users that created them
     """
    password = serializers.CharField(max_length=200, write_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Patient
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'country','age' , 'gender', 'password', 'owner']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['username', 'password']