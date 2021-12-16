from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, LogoutSerializer,  MovieSerializer,  MovieViewSerialize
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserAPI(generics.ListAPIView):
    queryset = CustomUser.object.all()
    serializer_class = UserSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": LoginSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LogoutAPI(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LogoutSerializer
    
class MovieCreateAPI(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Movie = serializer.save()
        return Response({
            "name": MovieSerializer(Movie, context=self.get_serializer_context()).data,
        })

class MovieViewAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieViewSerializer


