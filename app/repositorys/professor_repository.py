from app.models.professor import Professor
from app.database.sias_db import SessionLocal

def listar_professores():
    session = SessionLocal()
    professores = session.query(Professor).all()
    result = [professor.to_dict() for professor in professores]
    session.close()
    return result

def buscar_professor_por_id(professor_id):
    session = SessionLocal()
    professor = session.query(Professor).filter(Professor.id == professor_id).first()
    result = professor.to_dict() if professor else None
    session.close()
    return result

def buscar_professor_por_email(email):
    session = SessionLocal()
    professor = session.query(Professor).filter(Professor.email == email).first()
    result = professor.to_dict() if professor else None
    session.close()
    return result

def criar_professor(professor_data):
    session = SessionLocal()
    senha = professor_data.pop('senha', None)
    professor = Professor(**professor_data)
    professor.set_senha(senha) if senha else None
    session.add(professor)
    session.commit()
    session.refresh(professor)
    result = professor.to_dict()
    session.close()
    return result

def atualizar_professor(professor_id, professor_data):
    session = SessionLocal()
    professor = session.query(Professor).filter(Professor.id == professor_id).first()
    if not professor:
        session.close()
        return None
    for key, value in professor_data.items():
        setattr(professor, key, value)
    session.commit()
    session.refresh(professor)
    result = professor.to_dict()
    session.close()
    return result

def deletar_professor(professor_id):
    session = SessionLocal()
    professor = session.query(Professor).filter(Professor.id == professor_id).first()
    if not professor:
        session.close()
        return False
    session.delete(professor)
    session.commit()
    session.close()
    return True