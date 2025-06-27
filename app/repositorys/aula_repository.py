from app.models.aula import Aula
from app.database.sias_db import SessionLocal

def listar_aulas():
    session = SessionLocal()
    aulas = session.query(Aula).all()
    result = [aula.to_dict() for aula in aulas]
    session.close()
    return result

def buscar_aula_por_id(aula_id):
    session = SessionLocal()
    aula = session.query(Aula).filter(Aula.id == aula_id).first()
    result = aula.to_dict() if aula else None
    session.close()
    return result

def criar_aula(aula_data):
    session = SessionLocal()
    aula = Aula(**aula_data)
    session.add(aula)
    session.commit()
    session.refresh(aula)
    result = aula.to_dict()
    session.close()
    return result

def atualizar_aula(aula_id, aula_data):
    session = SessionLocal()
    aula = session.query(Aula).filter(Aula.id == aula_id).first()
    if not aula:
        session.close()
        return None
    for key, value in aula_data.items():
        setattr(aula, key, value)
    session.commit()
    session.refresh(aula)
    result = aula.to_dict()
    session.close()
    return result

def deletar_aula(aula_id):
    session = SessionLocal()
    aula = session.query(Aula).filter(Aula.id == aula_id).first()
    if not aula:
        session.close()
        return False
    session.delete(aula)
    session.commit()
    session.close()
    return True
