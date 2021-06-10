
from medic.models import Medic
from medic.serializers import MedicSerializer
from rest_framework import generics
from rest_framework import permissions
from medic.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
import jwt

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'medic': reverse('medic-list', request=request, format=format) 

    })



class MedicList(generics.ListCreateAPIView):
    """

    """
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    # TODO: implement and test authentication to uncomment the next line
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        serializer = MedicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

                      
        user = Medic.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        return Response  ({
            'message':'success'
        })
        


    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    def perform_create(self, serializer):
        """
    allows us to associate users with the instances they create 
    at the same time preventing the creation od duplicates
        """
        queryset = SignupRequest.objects.filter(user=self.request.user)
        if queryset.exists():
            raise ValidationError('You have already signed up')

        serializer.save(owner=self.request.user)
        
    

    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


class MedicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#lass RegisterView():
    pass
#