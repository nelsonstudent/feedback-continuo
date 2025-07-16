from datetime import datetime, timedelta
from app.models.material_aprendido import MaterialAprendido
from app.database import db

class MaterialAprendizadoService:
    @staticmethod
    def get_materiais_disponiveis(disciplina_id, aluno_id=None):
        # Materiais disponíveis até 48h antes da aula
        query = MaterialAprendido.query.filter(
            MaterialAprendido.disciplina_id == disciplina_id,
            MaterialAprendido.disponivel_de <= datetime.utcnow()
        ) .order_by(MaterialAprendido.class_date.asc()). all()

        if aluno_id:
            query = query.filter(MaterialAprendido.aluno_id == aluno_id)
        return query.all()

    @staticmethod
    def criar_material(disciplina_id, titulo, material_type, aluno_id, conteudo, class_date, disponivel_ate=None):
        # Disponibiliza 48h antes da aula
        disponivel_de = class_date - timedelta(hours=48)
        if not titulo or not material_type or not conteudo:
            raise ValueError("Titulo, tipo de material e conteúdo são obrigatórios")
        if not disciplina_id or not aluno_id:
            raise ValueError("Disciplina ID e Aluno ID são obrigatórios")
        if disponivel_ate and disponivel_ate < disponivel_de:
            raise ValueError("Data limite de disponibilidade não pode ser anterior à data de disponibilização")
       
        new_material = MaterialAprendido(
            aluno_id=aluno_id,
            conteudo=conteudo,
            disciplina_id=disciplina_id,
            titulo=titulo,
            material_type=material_type,
            disponivel_de=disponivel_de,
            disponivel_ate=disponivel_ate
        )
        db.session.add(new_material)
        db.session.commit()
        return new_material

    def get_materiais_by_disciplina(disciplina_id):
        return MaterialAprendido.query.filter_by(disciplina_id=disciplina_id).all()

    @staticmethod
    def get_materiais_by_aluno(aluno_id):
        return MaterialAprendido.query.filter_by(aluno_id=aluno_id).all()

    @staticmethod
    def add_material(aluno_id, conteudo, disciplina_id, titulo, material_type, disponivel_de, disponivel_ate=None):
        new_material = MaterialAprendido(
            aluno_id=aluno_id,
            conteudo=conteudo,
            disciplina_id=disciplina_id,
            titulo=titulo,
            material_type=material_type,
            disponivel_de=disponivel_de,
            disponivel_ate=disponivel_ate
        )
        db.session.add(new_material)
        db.session.commit()
        return new_material