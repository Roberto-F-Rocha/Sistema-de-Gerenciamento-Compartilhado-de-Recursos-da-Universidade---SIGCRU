from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from patrimonios.models import Patrimonio


class PatrimonioTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="123456")
        self.client.login(username="teste", password="123456")

        self.patrimonio_data = {
            "nome": "Computador Dell",
            "descricao": "Core i5, 8GB RAM",
            "situacao": "Ativo"
        }
        self.patrimonio = Patrimonio.objects.create(**self.patrimonio_data)
        self.url_base = "/api/patrimonios/"

    def test_criar_patrimonio(self):
        response = self.client.post(self.url_base, self.patrimonio_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_patrimonios(self):
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_patrimonio(self):
        url = f"{self.url_base}{self.patrimonio.id}/"
        response = self.client.put(url, {
            "nome": "Notebook Lenovo",
            "descricao": "Core i7, 16GB RAM",
            "situacao": "Em uso"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_patrimonio(self):
        url = f"{self.url_base}{self.patrimonio.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- Testes de autenticação ---
    def test_nao_autenticado_nao_pode_listar(self):
        self.client.logout()
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_criar(self):
        self.client.logout()
        response = self.client.post(self.url_base, self.patrimonio_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_atualizar(self):
        self.client.logout()
        url = f"{self.url_base}{self.patrimonio.id}/"
        response = self.client.put(url, {"nome": "Alteração sem login"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_deletar(self):
        self.client.logout()
        url = f"{self.url_base}{self.patrimonio.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
