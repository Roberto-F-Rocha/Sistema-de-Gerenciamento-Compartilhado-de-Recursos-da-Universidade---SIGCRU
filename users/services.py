from django.contrib.auth import authenticate, get_user_model

User = get_user_model()
class AuthenticationService:

    @staticmethod
    def autenticar_usuario_local(username: str, password: str):
        return authenticate(username=username, password=password)

    @staticmethod
    def autenticar_sigaa_ciape(username: str, password: str):
        if username.startswith("aluno") and password == "123":
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        return None

    @staticmethod
    def autenticar(username: str, password: str):
        # tenta institucional primeiro
        user = AuthenticationService.autenticar_sigaa_ciape(username, password)
        if user:
            return user

        # tenta local
        return AuthenticationService.autenticar_usuario_local(username, password)
