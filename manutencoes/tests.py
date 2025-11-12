from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from manutencoes.models import Manutencao


class ManutencaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="123456")
        self.client.login(username="teste", password="123456")

        self.manutencao_data = {
            "descricao": "Troca de filtro de ar",
            "data": "2025-11-10",
            "responsavel": "João",
            "status": "Pendente"
        }
        self.manutencao = Manutencao.objects.create(**self.manutencao_data)
        self.url_base = "/api/manutencoes/"

    def test_criar_manutencao(self):
        response = self.client.post(self.url_base, self.manutencao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_manutencoes(self):
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_manutencao(self):
        url = f"{self.url_base}{self.manutencao.id}/"
        response = self.client.put(url, {
            "descricao": "Filtro trocado",
            "data": "2025-11-11",
            "responsavel": "Carlos",
            "status": "Concluído"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_manutencao(self):
        url = f"{self.url_base}{self.manutencao.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- Testes de autenticação ---
    def test_nao_autenticado_nao_pode_listar(self):
        self.client.logout()
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_criar(self):
        self.client.logout()
        response = self.client.post(self.url_base, self.manutencao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_atualizar(self):
        self.client.logout()
        url = f"{self.url_base}{self.manutencao.id}/"
        response = self.client.put(url, {"descricao": "Alteração sem login"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_deletar(self):
        self.client.logout()
        url = f"{self.url_base}{self.manutencao.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
