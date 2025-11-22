from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Informações extras adicionadas ao JWT
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role  # caso tenha campo

        return token
