from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "tipo_usuario"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            tipo_usuario=validated_data.get("tipo_usuario")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['tipo_usuario'] = getattr(user, "tipo_usuario", None)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email,
                "tipo_usuario": getattr(self.user, "tipo_usuario", None),
                "is_staff": self.user.is_staff,
                "is_superuser": self.user.is_superuser,
            }
        })
        return data
