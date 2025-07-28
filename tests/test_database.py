import unittest
import importlib
import os
import sys
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

# Import Base from the app's database module
from app.database.sias_db import Base
from app.models import aluno, aula, aula_material, avaliacao, grupo_aula, material
from app.models import material_visualizado, pre_teste, professor, relatorio, resposta_pre_teste

class TestModelDatabaseIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

        # Create tables
        Base.metadata.create_all(cls.engine)

    def tearDown(self):
        self.session.rollback()

    # Aluno
    def test_insert_aluno(self):
        instance = aluno.Aluno(nome="Aluno Teste", email="aluno@example.com", turma="A", senha_hash="hash")
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_verificar_aluno(self):
        instance = aluno.Aluno(nome="Maria", email="maria@email.com", turma="B", senha_hash="senha")
        self.session.add(instance)
        self.session.commit()
        resultado = self.session.query(aluno.Aluno).filter_by(email="maria@email.com").first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nome, "Maria")

    # Aula
    def test_insert_aula(self):
        instance = aula.Aula(tema="Aula Teste", data=datetime.now())
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_verificar_aula(self):
        instance = aula.Aula(tema="Geografia", data=datetime.now())
        self.session.add(instance)
        self.session.commit()
        buscada = self.session.query(aula.Aula).filter_by(tema="Geografia").first()
        self.assertIsNotNone(buscada)
        self.assertEqual(buscada.tema, "Geografia")

    # Aula-Material
    def test_insert_aula_material(self):
        aula_instance = aula.Aula(tema="Tema Aula", data=datetime.now())
        material_instance = material.Material(titulo="Mat", tipo="pdf")
        self.session.add_all([aula_instance, material_instance])
        self.session.commit()
        stmt = aula_material.aula_material.insert().values(aula_id=aula_instance.id, material_id=material_instance.id)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        self.assertTrue(True)

    def test_verificar_aula_material(self):
        aula_instance = aula.Aula(tema="Biologia", data=datetime.now())
        material_instance = material.Material(titulo="Vídeo", tipo="video")
        self.session.add_all([aula_instance, material_instance])
        self.session.commit()
        stmt = aula_material.aula_material.insert().values(aula_id=aula_instance.id, material_id=material_instance.id)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        result = self.session.execute(
            aula_material.aula_material.select().where(aula_material.aula_material.c.material_id == material_instance.id)
        ).fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result.aula_id, aula_instance.id)

    # Avaliação
    def test_insert_avaliacao(self):
        aluno_instance = aluno.Aluno(nome="Carlos", email="carlos@email.com", turma="3C", senha_hash="senha")
        aula_instance = aula.Aula(tema="Física", data=datetime.now())
        self.session.add_all([aluno_instance, aula_instance])
        self.session.commit()
        instance = avaliacao.Avaliacao(tipo="final", nota_escala=9.5, comentarios="Excelente", aluno_id=aluno_instance.id, aula_id=aula_instance.id)
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_verificar_avaliacao(self):
        aluno_instance = aluno.Aluno(nome="Laura", email="laura@email.com", turma="4D", senha_hash="senha2")
        aula_instance = aula.Aula(tema="Química", data=datetime.now())
        self.session.add_all([aluno_instance, aula_instance])
        self.session.commit()
        instance = avaliacao.Avaliacao(tipo="parcial", nota_escala=7.0, comentarios="Boa", aluno_id=aluno_instance.id, aula_id=aula_instance.id)
        self.session.add(instance)
        self.session.commit()
        resultado = self.session.query(avaliacao.Avaliacao).filter_by(aluno_id=aluno_instance.id, aula_id=aula_instance.id).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.tipo, "parcial")

    # Outros modelos (sem alteração)
    def test_insert_grupo_aula(self):
        instance = grupo_aula.GrupoAula(codigo_turma="G123")
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_insert_material(self):
        instance = material.Material(titulo="Material 1", tipo="video")
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_insert_material_visualizado(self):
        aluno_instance = aluno.Aluno(nome="Aluno", email="a@b.com", turma="B", senha_hash="x")
        material_instance = material.Material(titulo="Mat", tipo="pdf")
        self.session.add_all([aluno_instance, material_instance])
        self.session.commit()
        instance = material_visualizado.MaterialVisualizado(aluno_id=aluno_instance.id, material_id=material_instance.id)
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_insert_pre_teste(self):
        instance = pre_teste.PreTeste(pergunta="Pergunta?")
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_insert_professor(self):
        instance = professor.Professor(nome="Prof Teste", email="prof@example.com", senha_hash="hash")
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_insert_relatorio(self):
        instance = relatorio.Relatorio()
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

    def test_insert_resposta_pre_teste(self):
        instance = resposta_pre_teste.RespostaPreTeste(resposta="Resposta")
        self.session.add(instance)
        self.session.commit()
        self.assertIsNotNone(instance.id)

if __name__ == '__main__':
    unittest.main()
