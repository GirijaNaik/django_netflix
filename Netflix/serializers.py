from rest_framework import serializers
from .models import CustomUser, Movie
from django.contrib.auth import get_user_model

# User Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

# Register Serializer
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
        return User.objects.create_user(validated_data['email'], validated_data['password'])

class LogoutSerializer(serializers.Serializer):
    pass

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=10)
    created = serializers.DateTimeField()
    uuid = serializers.UUIDField(default=uuid.uuid4)
    flyer = serializers.ImageField()
    def create(self, validated_data):
        movie = Movie.objects.create_movie(validated_data['title'], validated_data['type'], validated_data['created'], validated_data['uuid'], validated_data['flyer'])
        return movie

class MovieViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'type', 'created', 'uuid', 'flyer')

