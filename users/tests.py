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

    def test_login_com_usuario_valido(self):
        url = reverse("login")
        response = self.client.post(url, {
            "username": "teste",
            "password": "senha123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)

    def test_login_com_credenciais_invalidas(self):
        url = reverse("login")
        response = self.client.post(url, {
            "username": "teste",
            "password": "senha_errada"
        })

        self.assertEqual(response.status_code, 400)
