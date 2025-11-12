from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from solicitacoes.models import Solicitacao


class SolicitacaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="123456")
        self.client.login(username="teste", password="123456")

        self.solicitacao_data = {
            "titulo": "Reparo elétrico",
            "descricao": "Lâmpada queimada no corredor",
            "status": "Aberta"
        }
        self.solicitacao = Solicitacao.objects.create(**self.solicitacao_data)
        self.url_base = "/api/solicitacoes/"

    def test_criar_solicitacao(self):
        response = self.client.post(self.url_base, self.solicitacao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_solicitacoes(self):
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_solicitacao(self):
        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.put(url, {
            "titulo": "Reparo hidráulico",
            "descricao": "Torneira vazando na cozinha",
            "status": "Em andamento"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_solicitacao(self):
        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- Testes de autenticação ---
    def test_nao_autenticado_nao_pode_listar(self):
        self.client.logout()
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_criar(self):
        self.client.logout()
        response = self.client.post(self.url_base, self.solicitacao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_atualizar(self):
        self.client.logout()
        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.put(url, {"titulo": "Tentando sem login"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_deletar(self):
        self.client.logout()
        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
