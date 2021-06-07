
from medic.models import Medic
from medic.serializers import MedicSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from medic.serializers import UserSerializer
from rest_framework import permissions
from medic.permissions import IsOwnerOrReadOnly


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class MedicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

