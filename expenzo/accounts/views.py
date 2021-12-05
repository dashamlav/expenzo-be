from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.services.appUserService import appUserService
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

class LoginView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not (email and password):
            return Response(data={'message': "Username/Password not found."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if not user:
            return Response(data={'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={
            'message': 'User authenticated succesfully',
            'token': token.key
            }, 
            status=status.HTTP_200_OK)

       
class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        
        registerSerializer = RegisterSerializer(data=request.data)

        if not registerSerializer.is_valid():
            return Response(data={'message':'Insufficient information'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = registerSerializer.data['email']
        password = registerSerializer.data['password']
        name = registerSerializer.data['name']

        if appUserService.doesUserExist(email):
            return Response(data={'message':'Account already exists'}, status=status.HTTP_400_BAD_REQUEST)

        encrypted_password = make_password(password)
        createdUser = appUserService.createUser(name, email, encrypted_password)
        token, _ = Token.objects.get_or_create(user=createdUser)

        return Response(data={
            'message': 'User registered succesfully',
            'token': token.key
            }, 
            status=status.HTTP_200_OK)
        

class ValidateTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        
        email = request.data.get('email', None)
        token = request.data.get('token', None)

        if not(email and token):
            return Response(data={'message':'Insufficient information'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(key=token, user__email=email)
            return Response(data={'message': 'Token Valid'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response(data={'message': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)