from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

# User Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

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
