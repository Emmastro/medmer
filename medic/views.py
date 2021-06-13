
from medic.models import Medic
from medic.serializers import MedicSerializer
from rest_framework import generics
from rest_framework import permissions
from medic.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
import jwt, datetime


    

class MedicList(generics.ListCreateAPIView):
    """

    """
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
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utc(now)

        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt' : token
        }
        return Response

    def perform_create(self, serializer):
        """
    allows us to associate users with the instances they create 
    at the same time preventing the creation od duplicates
        """
        queryset = SignupRequest.objects.filter(user=self.request.user)
        if queryset.exists():
            raise ValidationError('You have already signed up')
        serializer.save(user=self.request.user)
        
        
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


class MedicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

