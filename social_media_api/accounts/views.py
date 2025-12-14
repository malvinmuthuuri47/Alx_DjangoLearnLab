from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer, FollowSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model
from posts.models import Post
from posts.serializers import PostSerializer

User = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserProfileView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        if (request.user.id == user_id):
            return Response(
                {"detail": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            target_user = self.get_queryset().get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        request.user.following.add(target_user)

        return Response(
            {"detail": f"You are now following {target_user.username}"},
            status=status.HTTP_200_OK
        )
        # serializer = FollowSerializer(
        #     data=request.data,
        #     context={'request': request}
        # )
        # serializer.is_valid(raise_exception=True)

        # target_user = User.objects.get(id=serializer.validated_data['user_id'])
        # request.user.following.add(target_user)

        # return Response(
        #     {"detail": f"You are now following {target_user.username}"},
        #     status=status.HTTP_200_OK
        # )

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        if request.user.id == user_id:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            target_user = self.get_queryset().get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target_user)
        return Response({"detail": f"You have unfollowed {target_user.username}"}, status=status.HTTP_200_OK)
        # serializer = FollowSerializer(
        #     data=request.data,
        #     context={'request': request}
        # )
        # serializer.is_valid(raise_exception=True)

        # target_user = User.objects.get(id=serializer.validated_data['user_id'])
        # request.user.following.remove(target_user)

        # return Response(
        #     {"detail": f"You unfollowed {target_user.username}"},
        #     status=status.HTTP_200_OK
        # )

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        # get all posts by users that the current user follows
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)