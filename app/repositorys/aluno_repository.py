from app.models.aluno import Aluno
from app.database.sias_db import SessionLocal

def listar_alunos():
    session = SessionLocal()
    alunos = session.query(Aluno).all()
    result = [aluno.to_dict() for aluno in alunos]
    session.close()
    return result

def buscar_aluno_por_id(aluno_id):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.id == aluno_id).first()
    result = aluno.to_dict() if aluno else None
    session.close()
    return result

def buscar_aluno_por_email(email):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.email == email).first()
    result = aluno.to_dict() if aluno else None
    session.close()
    return aluno


def criar_aluno(aluno_data):
    session = SessionLocal()
    senha = aluno_data.pop('senha', None)
    aluno = Aluno(**aluno_data)
    aluno.set_senha(senha) if senha else None
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    result = aluno.to_dict()
    session.close()
    return result

def atualizar_aluno(aluno_id, aluno_data):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        session.close()
        return None
    for key, value in aluno_data.items():
        setattr(aluno, key, value)
    session.commit()
    session.refresh(aluno)
    result = aluno.to_dict()
    session.close()
    return result

def deletar_aluno(aluno_id):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        session.close()
        return False
    session.delete(aluno)
    session.commit()
    session.close()
    return True