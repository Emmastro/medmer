from patient.models import Patient
from patient.serializers import PatientSerializer
from rest_framework import generics
from rest_framework import permissions


class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
