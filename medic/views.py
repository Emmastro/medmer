from medic.models import Medic
from medic.serializers import MedicSerializer
from medic.serializers import LoginSerializer
from rest_framework import generics
from rest_framework import permissions
from medic.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.reverse import reverse
import jwt, datetime
from django.contrib.auth.hashers import check_password



    
class RegisterView(generics.GenericAPIView):
    serializer_class = MedicSerializer

    def post(self, request):
        serializer = MedicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
       
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        
                      
        user = Medic.objects.all().filter(username=username)
       # print(user) #
        #print(username)
        print(password)
        print(Medic.objects.filter(username=username))
    

        if username != user:
            raise AuthenticationFailed('user not found!')
        
        
        pwd = Medic.objects.all().filter(password=password)
        
        if password != pwd:
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.values()[0]['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()

        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt' : token
        }
        return response
    
class Userview(generics.GenericAPIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated!')

        user = Medic.objects.filter(id=payload['id']).first()
        serializer = MedicSerializer(user)
        return Response(serializer.data)

class MedicList(generics.ListCreateAPIView):
    """

    """
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    
   
    # TODO: implement and test authentication to uncomment the next line
    #d
    #def perform_create(self, serializer):

        #"""
        #allows us to associate users with the instances they create 
        #at the same time preventing the creation od duplicates
        #"""
       # queryset = Medic.objects.filter(user=self.request.user)
        #if queryset.exists():
           #raise ValidationError('You have already signed up')
       # serializer.save(user=self.request.user)
        
        
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


class MedicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

