from rest_framework.response import Response
from rest_framework import generics, mixins

from .models import User
from .serializers import UserSerializer, LoginSerializer
# from .validators import validate_category, validate_product

class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        user = request.data

        # Create a user from the above data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "User created successfully", 'user': serializer.data})

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        user = request.data

        # Login a user from the above data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        
        return Response({"success": "User successfully logged in", 'user': serializer.data})
