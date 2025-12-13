from rest_framework import serializers
# from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            bio = validated_data.get('bio', ''),
            profile_picture = validated_data.get('profile_picture', None)
        )

        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")
        
        # Token rotation
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)

        return {
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        }