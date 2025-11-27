from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from patrimonios.models import Patrimonio
from solicitacoes.models import Solicitacao

User = get_user_model()

class SolicitacaoAPITests(APITestCase):

    def setUp(self):
        # Usuários
        self.user = User.objects.create_user(
            username="usuario",
            password="123456"
        )
        self.admin = User.objects.create_user(
            username="admin",
            password="admin123",
            is_staff=True
        )

        # Patrimônio utilizado nos testes
        self.patrimonio = Patrimonio.objects.create(
            nome="Projetor Sala 10",
            descricao="Projetor Epson",
            quantidade=1
        )

        # Solicitação criada pelo usuário
        self.solicitacao = Solicitacao.objects.create(
            usuario=self.user,
            patrimonio=self.patrimonio,
            tipo="manutencao",
            descricao="Projetor não liga",
        )

        self.url_base = "/api/solicitacoes/"
        self.url_minhas = "/api/solicitacoes/minhas/"

    # TESTES DE LISTAGEM

    def test_usuario_lista_apenas_as_suas_solicitacoes(self):
        self.client.login(username="usuario", password="123456")
        response = self.client.get(self.url_base)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_admin_lista_todas_as_solicitacoes(self):
        self.client.login(username="admin", password="admin123")

        # cria mais uma solicitação de outro usuário
        Solicitacao.objects.create(
            usuario=self.user,
            patrimonio=self.patrimonio,
            tipo="dano",
            descricao="Tela quebrada"
        )

        response = self.client.get(self.url_base)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_listar_minhas_solicitacoes(self):
        self.client.login(username="usuario", password="123456")
        response = self.client.get(self.url_minhas)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["usuario"], self.user.id)

    # TESTES DE CRIAÇÃO
    
    def test_criar_solicitacao(self):
        self.client.login(username="usuario", password="123456")

        nova = {
            "patrimonio": self.patrimonio.id,
            "tipo": "dano",
            "descricao": "Cabo rompido"
        }

        response = self.client.post(self.url_base, nova, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["usuario"], self.user.id)

    # TESTES DE ATUALIZAÇÃO

    def test_usuario_pode_atualizar_sua_solicitacao(self):
        self.client.login(username="usuario", password="123456")

        url = f"{self.url_base}{self.solicitacao.id}/"
        data = {
            "patrimonio": self.patrimonio.id,
            "tipo": "manutencao",
            "descricao": "Atualizando descrição",
            "status": "em_analise"
        }

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "em_analise")

    def test_usuario_nao_pode_atualizar_de_outro_usuario(self):
        outro = User.objects.create_user(username="outro", password="abc123")
        self.client.login(username="outro", password="abc123")

        url = f"{self.url_base}{self.solicitacao.id}/"

        response = self.client.put(url, {
            "descricao": "Tentando alterar"
        }, format="json")

        self.assertEqual(response.status_code, 403)

    # TESTES DE DELETE
    
    def test_usuario_deleta_sua_solicitacao(self):
        self.client.login(username="usuario", password="123456")

        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

    def test_usuario_nao_deleta_solicitacao_de_outro(self):
        self.client.login(username="admin", password="admin123")

        outro_user = User.objects.create_user(
            username="xpto",
            password="senha"
        )

        solic = Solicitacao.objects.create(
            usuario=outro_user,
            patrimonio=self.patrimonio,
            tipo="falta",
            descricao="Fonte sumiu"
        )

        # admin pode deletar, usuário comum NÃO
        self.client.login(username="usuario", password="123456")
        url = f"{self.url_base}{solic.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)

    # TESTES DE AUTENTICAÇÃO
    
    def test_nao_autenticado_nao_pode_listar(self):
        response = self.client.get(self.url_base)
        self.assertEqual(response.status_code, 401)

    def test_nao_autenticado_nao_pode_criar(self):
        response = self.client.post(self.url_base, {}, format="json")
        self.assertEqual(response.status_code, 401)

    def test_nao_autenticado_nao_pode_atualizar(self):
        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.put(url, {
            "descricao": "Tentando"
        })
        self.assertEqual(response.status_code, 401)

    def test_nao_autenticado_nao_pode_deletar(self):
        url = f"{self.url_base}{self.solicitacao.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)
