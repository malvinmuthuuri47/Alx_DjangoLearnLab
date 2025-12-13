from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .models import CustomUser

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)

    #     # After registration, create a token
    #     user = CustomUser.objects.get(id=response.data['id'])
    #     token, created = Token.objects.get_or_create(user=user)

    #     return Response({
    #         "user": response.data,
    #         "token": token.key
    #     }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

        # username = serializer.validated_data['username']
        # password = serializer.validated_data['password']

        # user = authenticate(username=username, password=password)

        # if not user:
        #     return Response({"detail": "Invalid credentials"}, status=400)
        
        # token, created = Token.objects.get_or_create(user=user)

        # return Response({
        #     "token": token.key,
        #     "user": {
        #         "id": user.id,
        #         "username": user.username,
        #         "email": user.email,
        #     }
        # })