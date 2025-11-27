from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from patrimonios.models import Patrimonio, EspacoFisico

class PatrimonioEspacoFisicoTests(APITestCase):
    def setUp(self):
        # Usuário para autenticação
        self.user = User.objects.create_user(username="teste", password="123456")
        self.client.login(username="teste", password="123456")

        # Dados iniciais
        self.patrimonio_data = {
            "nome": "Computador Dell",
            "descricao": "Core i5, 8GB RAM",
            "status": "ativo"
        }

        self.espaco_data = {
            "nome": "Laboratório de Informática",
            "tipo": "laboratório"
        }

        # Criação de instâncias
        self.patrimonio = Patrimonio.objects.create(**self.patrimonio_data)
        self.espaco = EspacoFisico.objects.create(**self.espaco_data)
        
        # URLs base
        self.url_patrimonio = "/api/patrimonios/"
        self.url_espaco = "/api/patrimonios/espacos-fisicos/"

    # --- Testes Patrimônio ---
    def test_criar_patrimonio(self):
        response = self.client.post(self.url_patrimonio, self.patrimonio_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_patrimonios(self):
        response = self.client.get(self.url_patrimonio)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_patrimonio(self):
        url = f"{self.url_patrimonio}{self.patrimonio.id}/"
        response = self.client.put(url, {
            "nome": "Notebook Lenovo",
            "descricao": "Core i7, 16GB RAM",
            "status": "inativo"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_patrimonio(self):
        url = f"{self.url_patrimonio}{self.patrimonio.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- Testes Espaços Físicos ---
    def test_criar_espaco(self):
        response = self.client.post(self.url_espaco, self.espaco_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_espacos(self):
        response = self.client.get(self.url_espaco)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_espaco(self):
        url = f"{self.url_espaco}{self.espaco.id}/"
        response = self.client.put(url, {"nome": "Auditório Principal", "tipo": "auditório"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_espaco(self):
        url = f"{self.url_espaco}{self.espaco.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- Testes de autenticação ---
    def test_nao_autenticado_nao_pode_listar(self):
        self.client.logout()
        response_patrimonio = self.client.get(self.url_patrimonio)
        response_espaco = self.client.get(self.url_espaco)
        self.assertEqual(response_patrimonio.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_espaco.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_nao_autenticado_nao_pode_criar(self):
        self.client.logout()
        response_patrimonio = self.client.post(self.url_patrimonio, self.patrimonio_data, format="json")
        response_espaco = self.client.post(self.url_espaco, self.espaco_data, format="json")
        self.assertEqual(response_patrimonio.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_espaco.status_code, status.HTTP_401_UNAUTHORIZED)
