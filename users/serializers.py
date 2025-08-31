from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]
        read_only_fields = ["id"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        return User.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        return user
