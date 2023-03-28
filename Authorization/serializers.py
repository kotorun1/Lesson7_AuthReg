from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(read_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
                
        def save(self, **kwargs):
            user = User(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
            )
            password = self.validated_data['password']
            password2 = self.validated_data['password2']
            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match.'})    
            user.set_password(password)
            user.save()

            def __init__(self):
                self.user = user
            
            return self.user
            

class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                return user
            else:
                raise serializers.ValidationError('User is not active.')
        else:
            raise serializers.ValidationError('User not found.')