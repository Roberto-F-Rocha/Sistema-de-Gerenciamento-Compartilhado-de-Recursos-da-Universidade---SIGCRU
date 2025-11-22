# users/services.py

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AuthenticationService:

    @staticmethod
    def autenticar_usuario_local(username: str, password: str):
        user = authenticate(username=username, password=password)
        return user

    @staticmethod
    def autenticar_sigaa_ciape(username: str, password: str):

        if username.startswith("aluno") and password == "123":
            # Você pode consultar no seu banco se este username existe:
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        return None

    @staticmethod
    def autenticar(username: str, password: str):
        #Tenta autenticação SIGAA/CIAPE
        user = AuthenticationService.autenticar_sigaa_ciape(username, password)

        if user:
            return user

        #Tenta autenticação local
        user = AuthenticationService.autenticar_usuario_local(username, password)

        return user
