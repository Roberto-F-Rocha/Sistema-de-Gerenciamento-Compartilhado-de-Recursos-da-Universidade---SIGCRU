from rest_framework import serializers
from users.services import AuthenticationService

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = AuthenticationService.autenticar(username, password)

        if not user:
            raise serializers.ValidationError("Credenciais inválidas.")

        attrs["user"] = user
        return attrs
