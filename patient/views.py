from patient.models import Patient
from patient.serializers import PatientSerializer
from patient.serializers import LoginSerializer
from rest_framework import generics
from rest_framework import permissions
from patient.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.reverse import reverse
import jwt, datetime
from django.contrib.auth.hashers import check_password



    
class RegisterView(generics.GenericAPIView):
    serializer_class = PatientSerializer

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
       
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        
                      
        user = Patient.objects.all().filter(username=username)
       # print(user) #
        #print(username)
        print(password)
        print(Patient.objects.filter(username=username))
    

        if user is None:
            raise AuthenticationFailed('user not found!')
        else:
        
            pwd = user.values()[0]['password']
        
            if password != pwd:
                raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.values()[0]['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()

        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') #.decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt' : token
        }
        return response

class PatientList(generics.ListCreateAPIView):
    """

    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
   
    # TODO: implement and test authentication to uncomment the next line
    #d
    #def perform_create(self, serializer):

        #"""
        #allows us to associate users with the instances they create 
        #at the same time preventing the creation od duplicates
        #"""
       # queryset = Patient.objects.filter(user=self.request.user)
        #if queryset.exists():
           #raise ValidationError('You have already signed up')
       # serializer.save(user=self.request.user)
        
        
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
