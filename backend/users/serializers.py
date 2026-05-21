from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user and hash the password
        user = User.objects.create_user(**validated_data)
        user.is_citizen = True  # Default to citizen for new signups
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Django's built-in authenticate function hashes the incoming password 
        # and checks if it matches the database.
        user = authenticate(username=data.get('username'), password=data.get('password'))
        
        if user and user.is_active:
            return user
            
        raise serializers.ValidationError("Incorrect username or password.")    