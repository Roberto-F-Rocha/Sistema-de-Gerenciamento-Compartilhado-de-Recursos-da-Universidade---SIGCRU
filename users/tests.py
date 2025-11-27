from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="teste",
            email="teste@example.com",
            password="senha123"
        )
        self.login_url = reverse("login")
        self.refresh_url = reverse("token_refresh")  # caso use JWT padrão
        # ajuste se o nome da rota for diferente

    def test_login_com_usuario_valido(self):
        response = self.client.post(self.login_url, {
            "username": "teste",
            "password": "senha123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)

        # Verificando dados do usuário
        user_data = response.data["user"]
        self.assertEqual(user_data["username"], "teste")
        self.assertEqual(user_data["email"], "teste@example.com")

    def test_login_com_credenciais_invalidas(self):
        response = self.client.post(self.login_url, {
            "username": "teste",
            "password": "senha_errada"
        })
        self.assertEqual(response.status_code, 400)

    def test_login_sem_username(self):
        response = self.client.post(self.login_url, {
            "password": "senha123"
        })
        self.assertEqual(response.status_code, 400)

    def test_login_sem_password(self):
        response = self.client.post(self.login_url, {
            "username": "teste"
        })
        self.assertEqual(response.status_code, 400)

    def test_access_token_funciona_em_rota_protegida(self):
        # Login
        login = self.client.post(self.login_url, {
            "username": "teste",
            "password": "senha123"
        })

        access = login.data["access"]

        # Exemplo de rota protegida — ajuste conforme seu projeto
        protected_url = reverse("user-list")

        # Enviando token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        response = self.client.get(protected_url)

        # Token válido NÃO deve retornar 401
        self.assertNotEqual(response.status_code, 401)
        self.assertIn(response.status_code, [200, 403])
        # depende das permissões da rota

    def test_refresh_token_retorna_novo_access(self):
        login = self.client.post(self.login_url, {
            "username": "teste",
            "password": "senha123"
        })

        refresh = login.data["refresh"]

        response = self.client.post(self.refresh_url, {"refresh": refresh})

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_refresh_token_invalido(self):
        response = self.client.post(self.refresh_url, {"refresh": "tokeninvalido"})
        self.assertEqual(response.status_code, 401)
