from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from patrimonios.models import Patrimonio
from manutencoes.models import Manutencao


class ManutencaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="123456")
        self.client.login(username="teste", password="123456")

        # Patrimônio é obrigatório no modelo
        self.patrimonio = Patrimonio.objects.create(
            nome="Computador Dell",
            descricao="Máquina teste",
            numero_tombo="12345"
        )

        self.manutencao_data = {
            "patrimonio": self.patrimonio.id,
            "usuario": self.user.id,
            "descricao": "Troca de filtro de ar",
            "data_inicio": "2025-11-10",
            "data_fim": None,
            "status": "pendente"
        }

        self.manutencao = Manutencao.objects.create(
            patrimonio=self.patrimonio,
            usuario=self.user,
            descricao="Troca de filtro de ar",
            data_inicio="2025-11-10",
            status="pendente"
        )

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
            "patrimonio": self.patrimonio.id,
            "usuario": self.user.id,
            "descricao": "Filtro trocado",
            "data_inicio": "2025-11-11",
            "data_fim": "2025-11-12",
            "status": "concluida"
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
