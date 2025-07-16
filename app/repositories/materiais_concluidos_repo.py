from app.models.materiais_concluidos import MateriaisConcluidos
from app import db

def marcar_concluido(material_id, aluno_id):
    material = MateriaisConcluidos.query.filter_by(id=material_id, aluno_id=aluno_id).first()
    if not material:
        return None
    material.concluido = True
    db.session.commit()
    return material

def listar_concluidos(aluno_id):
    return MateriaisConcluidos.query.filter_by(aluno_id=aluno_id, concluido=True).all()
