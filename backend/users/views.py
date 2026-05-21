from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import UserRegistrationSerializer, UserLoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    # 1. 👈 Add this line to bypass DRF's strict CSRF session checks just for logging in
    authentication_classes = [] 

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user) # Creates the session cookie
            
            # Send ALL role flags back to React
            return Response({
                "message": "Login successful!",
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "is_admin": user.is_admin,
                    "is_driver": user.is_driver,
                    "is_citizen": user.is_citizen,
                    "is_superuser": user.is_superuser
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)