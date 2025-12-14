from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username = validated_data['username'],
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

class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'bio',
            'profile_picture',
            'followers_count'
        ]

        read_only_fields = ['username', 'followers_count']
    
    def get_followers_count(self, obj):
        if (hasattr(obj, 'followers')):
            return obj.followers.count()
        
        return 0

class FollowSerializer(APIView):
    user_id = serializers.IntegerField()

    def validate_user_id(self, value):
        request = self.context['request']
        if request.user.id == value:
            raise serializers.ValidationError("You cannot follow yourself.")
        
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User does not exist.")
        
        return value
    # permission_classes = [IsAuthenticated]

    # def post(self, request, user_id):
    #     serializer = FollowSerializer(
    #         data={'user_id': user_id},
    #         context={'request': request}
    #     )

    #     serializer.is_valid(raise_exception=True)

    #     target_user = User.objects.get(id=serializer.validated_data['user_id'])
    #     request.user.following.add(target_user)

    #     return Response(
    #         {"detail": "Followed successfully"},
    #         status=status.HTTP_200_OK
    #     )
    # user_id = serializers.IntegerField()

    # def validate_user_id(self, value):
    #     request = self.context['request']
    #     if request.user.id == value:
    #         raise serializers.ValidationError("You cannot follow yourself.")
        
    #     if not User.objects.filter(id=value).exists():
    #         raise serializers.ValidationError("User does not exist.")
    
    #     return value