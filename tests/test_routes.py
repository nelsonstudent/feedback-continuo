import unittest
from unittest.mock import patch
import json

from app.main import create_app
from app.database.sias_db import Base, engine, SessionLocal
from app.models.aluno import Aluno
from app.models.aula import Aula
from datetime import datetime

class AlunoRoutesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(testing=True)
        cls.client = cls.app.test_client()
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        cls.db = SessionLocal()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
        Base.metadata.drop_all(bind=engine)

    def setUp(self):
        self.db.rollback()
        self.db.query(Aluno).delete()
        self.db.query(Aula).delete()
        self.db.commit()

        aluno = Aluno(nome="Teste", email="teste@ex.com", turma="1A")
        aluno.set_senha("123")
        self.db.add(aluno)

        aula = Aula(tema="Aula Teste", data=datetime.strptime("2024-01-01", "%Y-%m-%d"))
        self.db.add(aula)

        self.db.commit()
        self.db.refresh(aluno)
        self.db.refresh(aula)
        self.aluno_id = aluno.id
        self.aula_id = aula.id

    def tearDown(self):
        self.db.rollback()

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_listar_alunos(self):
        res = self.client.get('/alunos/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_buscar_aluno(self):
        res = self.client.get(f'/alunos/{self.aluno_id}')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['email'], 'teste@ex.com')

    def test_criar_aluno(self):
        payload = {
            "nome": "Novo Aluno",
            "email": "novo@ex.com",
            "senha": "123",
            "confirmacao_senha": "123",
            "turma": "1B"
        }
        res = self.client.post('/alunos/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_criar_aluno_faltando_campos(self):
        payload = {"email": "semnome@ex.com"}
        res = self.client.post('/alunos/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 400)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_atualizar_aluno(self):
        payload = {"nome": "Atualizado"}
        res = self.client.put(f'/alunos/{self.aluno_id}', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['nome'], 'Atualizado')

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_deletar_aluno(self):
        res = self.client.delete(f'/alunos/{self.aluno_id}')
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    def test_listar_aulas(self):
        res = self.client.get('/aulas/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    def test_buscar_aula(self):
        res = self.client.get(f'/aulas/{self.aula_id}')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['tema'], 'Aula Teste')

    def test_criar_aula(self):
        res = self.client.post(
            '/aulas/',
            data=json.dumps({
                "tema": "Nova Aula",
                "data": datetime(2025, 7, 28).strftime("%Y-%m-%dT%H:%M:%S")
            }),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)

    def test_atualizar_aula(self):
        res = self.client.put(
            f'/aulas/{self.aula_id}',
            data=json.dumps({"tema": "Tema Atualizado"}),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["tema"], "Tema Atualizado")

    def test_deletar_aula(self):
        res = self.client.delete(f'/aulas/{self.aula_id}')
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    @patch("app.routes.auth_route.buscar_aluno_por_email")
    @patch("app.routes.auth_route.buscar_professor_por_email")
    @patch("app.routes.auth_route.create_access_token")
    def test_login_aluno_com_sucesso(self, mock_create_token, mock_buscar_professor, mock_buscar_aluno):
        class MockUser:
            id = 1
            nome = "Aluno Teste"
            def verificar_senha(self, s): return s == "123"
        mock_buscar_aluno.return_value = MockUser()
        mock_create_token.return_value = "fake-token"
        res = self.client.post("/login", json={"email": "teste@ex.com", "senha": "123"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["access_token"], "fake-token")

    @patch("app.routes.auth_route.buscar_aluno_por_email", return_value=None)
    @patch("app.routes.auth_route.buscar_professor_por_email")
    def test_login_credenciais_invalidas(self, mock_buscar_professor, _):
        mock_buscar_professor.return_value = None
        res = self.client.post("/login", json={"email": "nao@ex.com", "senha": "errada"})
        self.assertEqual(res.status_code, 401)
        self.assertIn("msg", res.get_json())

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.avaliacao_route.listar_avaliacoes_service", return_value=[])
    def test_listar_avaliacoes(self, _):
        res = self.client.get("/avaliacoes/")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.avaliacao_route.buscar_avaliacao_por_id_service", return_value={"id": 1, "nota": 8})
    def test_buscar_avaliacao(self, _):
        res = self.client.get("/avaliacoes/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["id"], 1)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.avaliacao_route.criar_avaliacao_service", return_value={"id": 1, "nota": 9})
    def test_criar_avaliacao(self, _):
        res = self.client.post("/avaliacoes/", json={"nota": 9})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()["nota"], 9)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.avaliacao_route.atualizar_avaliacao_service", return_value={"id": 1, "nota": 10})
    def test_atualizar_avaliacao(self, _):
        res = self.client.put("/avaliacoes/1", json={"nota": 10})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nota"], 10)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.avaliacao_route.deletar_avaliacao_service", return_value=True)
    def test_deletar_avaliacao(self, _):
        res = self.client.delete("/avaliacoes/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.grupo_aula_route.listar_grupos_aula_service", return_value=[])
    def test_listar_grupo_aula(self, _):
        res = self.client.get("/grupo_aula/")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.grupo_aula_route.buscar_grupo_aula_por_id_service", return_value={"id": 1, "nome": "Grupo A"})
    def test_buscar_grupo_aula(self, _):
        res = self.client.get("/grupo_aula/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Grupo A")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.grupo_aula_route.criar_grupo_aula_service", return_value={"id": 1, "nome": "Grupo Novo"})
    def test_criar_grupo_aula(self, _):
        res = self.client.post("/grupo_aula/", json={"nome": "Grupo Novo"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()["nome"], "Grupo Novo")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.grupo_aula_route.atualizar_grupo_aula_service", return_value={"id": 1, "nome": "Grupo Atualizado"})
    def test_atualizar_grupo_aula(self, _):
        res = self.client.put("/grupo_aula/1", json={"nome": "Grupo Atualizado"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Grupo Atualizado")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.grupo_aula_route.deletar_grupo_aula_service", return_value=True)
    def test_deletar_grupo_aula(self, _):
        res = self.client.delete("/grupo_aula/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_route.listar_materiais_service", return_value=[])
    def test_listar_materiais(self, _):
        res = self.client.get("/materiais/")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_route.buscar_material_por_id_service", return_value={"id": 1, "nome": "Livro"})
    def test_buscar_material(self, _):
        res = self.client.get("/materiais/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Livro")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_route.criar_material_service", return_value={"id": 1, "nome": "Caderno"})
    def test_criar_material(self, _):
        res = self.client.post("/materiais/", json={"nome": "Caderno"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()["nome"], "Caderno")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_route.atualizar_material_service", return_value={"id": 1, "nome": "Caneta"})
    def test_atualizar_material(self, _):
        res = self.client.put("/materiais/1", json={"nome": "Caneta"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Caneta")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_route.deletar_material_service", return_value=True)
    def test_deletar_material(self, _):
        res = self.client.delete("/materiais/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_visualizado_route.listar_material_visualizado_service", return_value=[])
    def test_listar_material_visualizado(self, _):
        res = self.client.get("/material_visualizado/")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_visualizado_route.buscar_material_visualizado_por_id_service", return_value={"id": 1, "nome": "Slide Aula"})
    def test_buscar_material_visualizado(self, _):
        res = self.client.get("/material_visualizado/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Slide Aula")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_visualizado_route.criar_material_visualizado_service", return_value={"id": 1, "nome": "Video Aula"})
    def test_criar_material_visualizado(self, _):
        res = self.client.post("/material_visualizado/", json={"nome": "Video Aula"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()["nome"], "Video Aula")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_visualizado_route.atualizar_material_visualizado_service", return_value={"id": 1, "nome": "Apostila"})
    def test_atualizar_material_visualizado(self, _):
        res = self.client.put("/material_visualizado/1", json={"nome": "Apostila"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Apostila")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.material_visualizado_route.deletar_material_visualizado_service", return_value=True)
    def test_deletar_material_visualizado(self, _):
        res = self.client.delete("/material_visualizado/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.pre_teste_route.listar_pre_testes_service", return_value=[])
    def test_listar_pre_testes(self, _):
        res = self.client.get("/pre_testes/")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.pre_teste_route.buscar_pre_teste_por_id_service", return_value={"id": 1, "nome": "Pré-teste 1"})
    def test_buscar_pre_teste(self, _):
        res = self.client.get("/pre_testes/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Pré-teste 1")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.pre_teste_route.criar_pre_teste_service", return_value={"id": 1, "nome": "Pré-teste Criado"})
    def test_criar_pre_teste(self, _):
        res = self.client.post("/pre_testes/", json={"nome": "Pré-teste Criado"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()["nome"], "Pré-teste Criado")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.pre_teste_route.atualizar_pre_teste_service",
           return_value={"id": 1, "nome": "Pré-teste Atualizado"})
    def test_atualizar_pre_teste(self, _):
        res = self.client.put("/pre_testes/1", json={"nome": "Pré-teste Atualizado"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["nome"], "Pré-teste Atualizado")

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    @patch("app.routes.pre_teste_route.deletar_pre_teste_service", return_value=True)
    def test_deletar_pre_teste(self, _):
        res = self.client.delete("/pre_testes/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("mensagem", res.get_json())

    @patch("app.routes.professor_route.listar_professores_service", return_value=[{"id": 1, "nome": "Prof. João"}])
    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_listar_professores(self, mock_service):
        res = self.app.get("/professores/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), [{"id": 1, "nome": "Prof. João"}])

    @patch("app.routes.professor_route.criar_professor_service", return_value={"id": 1, "nome": "Prof. Novo"})
    def test_criar_professor(self, mock_service):
        res = self.app.post("/professores/", json={"nome": "Prof. Novo"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json(), {"id": 1, "nome": "Prof. Novo"})

    @patch("app.routes.professor_route.buscar_professor_por_id_service", return_value={"id": 1, "nome": "Prof. João"})
    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_buscar_professor(self, mock_service):
        res = self.app.get("/professores/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"id": 1, "nome": "Prof. João"})

    @patch("app.routes.professor_route.atualizar_professor_service", return_value={"id": 1, "nome": "Prof. Atualizado"})
    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_atualizar_professor(self, mock_service):
        res = self.app.put("/professores/1", json={"nome": "Prof. Atualizado"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"id": 1, "nome": "Prof. Atualizado"})

    @patch("app.routes.professor_route.deletar_professor_service", return_value=True)
    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request", lambda *args, **kwargs: None)
    def test_deletar_professor(self, mock_service):
        res = self.app.delete("/professores/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"mensagem": "Professor deletado com sucesso"})

    @patch("app.routes.relatorio_route.listar_relatorios_service", return_value=[{"id": 1, "titulo": "Relatório A"}])
    def test_listar_relatorios(self, mock_service):
        res = self.app.get("/relatorios/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), [{"id": 1, "titulo": "Relatório A"}])

    @patch("app.routes.relatorio_route.buscar_relatorio_por_id_service",
           return_value={"id": 1, "titulo": "Relatório A"})
    def test_buscar_relatorio(self, mock_service):
        res = self.app.get("/relatorios/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"id": 1, "titulo": "Relatório A"})

    @patch("app.routes.relatorio_route.criar_relatorio_service", return_value={"id": 1, "titulo": "Relatório Criado"})
    def test_criar_relatorio(self, mock_service):
        res = self.app.post("/relatorios/", json={"titulo": "Relatório Criado"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json(), {"id": 1, "titulo": "Relatório Criado"})

    @patch("app.routes.relatorio_route.atualizar_relatorio_service", return_value={"id": 1, "titulo": "Atualizado"})
    def test_atualizar_relatorio(self, mock_service):
        res = self.app.put("/relatorios/1", json={"titulo": "Atualizado"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"id": 1, "titulo": "Atualizado"})

    @patch("app.routes.relatorio_route.deletar_relatorio_service", return_value=True)
    def test_deletar_relatorio(self, mock_service):
        res = self.app.delete("/relatorios/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"mensagem": "Entidade deletada com sucesso"})

    @patch("app.routes.resposta_pre_teste_route.listar_respostas_pre_teste", return_value=[{"id": 1}])
    def test_listar_respostas_pre_teste(self, mock_service):
        res = self.app.get("/respostas_pre_teste/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), [{"id": 1}])

    @patch("app.routes.resposta_pre_teste_route.buscar_resposta_pre_teste_por_id", return_value={"id": 1})
    def test_buscar_resposta_pre_teste(self, mock_service):
        res = self.app.get("/respostas_pre_teste/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"id": 1})

    @patch("app.routes.resposta_pre_teste_route.criar_resposta_pre_teste",
           return_value={"id": 1, "resposta": "resposta"})
    def test_criar_resposta_pre_teste(self, mock_service):
        res = self.app.post("/respostas_pre_teste/", json={"resposta": "resposta"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json(), {"id": 1, "resposta": "resposta"})

    @patch("app.routes.resposta_pre_teste_route.atualizar_resposta_pre_teste_service",
           return_value={"id": 1, "resposta": "nova"})
    def test_atualizar_resposta_pre_teste(self, mock_service):
        res = self.app.put("/respostas_pre_teste/1", json={"resposta": "nova"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"id": 1, "resposta": "nova"})

    @patch("app.routes.resposta_pre_teste_route.deletar_resposta_pre_teste_service", return_value=True)
    def test_deletar_resposta_pre_teste(self, mock_service):
        res = self.app.delete("/respostas_pre_teste/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"mensagem": "Deletado com sucesso"})

if __name__ == '__main__':
    unittest.main()
