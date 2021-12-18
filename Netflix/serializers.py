from rest_framework import serializers
from .models import CustomUser, Movie, Upcoming_movie, Top_rated, comedy_movies, romantic_movies, action_movies, horror_movies, kids_movies
from django.contrib.auth import get_user_model

# User Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        return user

class LogoutSerializer(serializers.Serializer):
    pass

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class Upcoming_movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcoming_movie
        fields = '__all__'

class Upcoming_movieViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcoming_movie
        fields = '__all__'

class Top_rated_movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_rated
        fields = '__all__'

class Top_rated_movieViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_rated
        fields = '__all__'

class comedy_moviesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = comedy_movies
        fields = '__all__'

class romantic_moviesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = romantic_movies
        fields = '__all__'


class action_moviesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = action_movies
        fields = '__all__'

class horror_moviesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = horror_movies
        fields = '__all__'

class kids_moviesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = kids_movies
        fields = '__all__'



