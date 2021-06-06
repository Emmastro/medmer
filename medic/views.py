
from medic.models import Medic
from medic.serializers import MedicSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from medic.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MedicList(generics.ListCreateAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class MedicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer

