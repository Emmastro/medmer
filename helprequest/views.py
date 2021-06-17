from helprequest.models import HelpRequest
from patient.serializers import PatientSerializer
from helprequest.serializers import HelpRequestSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response


class HelpRequestList(generics.ListCreateAPIView):
    """
    Get: returns the list of help requests of a given patient \n
    Post: save a new help request
    """

    serializer_class = HelpRequestSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = HelpRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PatientHelpRequestList(generics.ListCreateAPIView):
    """returns the list of help requests of a given patient"""

    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, patient_id):
        queryset = HelpRequest.objects.get(patient__id=patient_id)
        return Response(queryset)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MedicHelpRequestList(generics.ListCreateAPIView):
    """returns the list of help requests of a given medic"""
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, medic_id):
        queryset = HelpRequest.objects.get(medic__id=medic_id)
        return Response(queryset)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    


class HelpRequestDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        """returns details of a specific help request """
        queryset = HelpRequest.objects.get(pk=pk)
        return Response(queryset)
