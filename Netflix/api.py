from rest_framework import generics, status,  permissions
from knox.models import AuthToken
from .models import CustomUser, Movie, Upcoming_movie, Top_rated, comedy_movies, romantic_movies, action_movies, horror_movies, kids_movies
from .serializers import UserSerializer, RegisterSerializer, MovieSerializer, LoginSerializer, MovieViewSerializer, Upcoming_movieSerializer, Upcoming_movieViewSerializer, Top_rated_movieSerializer
from rest_framework.response import Response
from .serializers import Top_rated_movieViewSerializer, comedy_moviesViewSerializer, romantic_moviesViewSerializer, action_moviesViewSerializer, horror_moviesViewSerializer, kids_moviesViewSerializer
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
    
class Upcoming_moviesAPI(generics.CreateAPIView):
    queryset = Upcoming_movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Movie = serializer.save()
        return Response({
            "name": Upcoming_movieSerializer(Movie, context=self.get_serializer_context()).data,
        })

class Upcoming_moviesViewAPI(generics.ListAPIView):
    queryset = Upcoming_movie.objects.all()
    serializer_class = Upcoming_movieViewSerializer

class Top_rated_movieAPI(generics.CreateAPIView):
    queryset = Top_rated.objects.all()
    serializer_class = Top_rated_movieSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Movie = serializer.save()
        return Response({
            "name": Top_rated_movieSerializer(Movie, context=self.get_serializer_context()).data,
        })

class Top_rated_movieViewAPI(generics.ListAPIView):
    queryset = Top_rated.objects.all()
    serializer_class = Top_rated_movieViewSerializer

class comedy_moviesViewAPI(generics.ListAPIView):
    queryset = comedy_movies.objects.all()
    serializer_class = comedy_moviesViewSerializer

class romantic_moviesViewAPI(generics.ListAPIView):
    queryset = romantic_movies.objects.all()
    serializer_class = romantic_moviesViewSerializer

class action_moviesViewAPI(generics.ListAPIView):
    queryset = action_movies.objects.all()
    serializer_class = action_moviesViewSerializer

class horror_moviesViewAPI(generics.ListAPIView):
    queryset = horror_movies.objects.all()
    serializer_class = horror_moviesViewSerializer

class kids_moviesViewAPI(generics.ListAPIView):
    queryset = kids_movies.objects.all()
    serializer_class = kids_moviesViewSerializer



