
from medic.models import Medic
from medic.serializers import MedicSerializer
from rest_framework import generics
from rest_framework import permissions
from medic.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class MedicList(generics.ListCreateAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    # TODO: implement and test authentication to uncomment the next line
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = Medic.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        return Response(user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
    

    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


class MedicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

