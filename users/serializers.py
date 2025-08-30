from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        return User.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"]
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        return user


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token["id"] = str(user.id)
#         token["email"] = user.email  # optional
#         token["name"] = user.name

#         return token
