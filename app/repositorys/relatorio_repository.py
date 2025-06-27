from app.models.relatorio import Relatorio
from app.database.sias_db import SessionLocal

def listar_relatorios():
    session = SessionLocal()
    relatorios = session.query(Relatorio).all()
    result = [relatorio.to_dict() for relatorio in relatorios]
    session.close()
    return result

def buscar_relatorio_por_id(relatorio_id):
    session = SessionLocal()
    relatorio = session.query(Relatorio).filter(Relatorio.id == relatorio_id).first()
    result = relatorio.to_dict() if relatorio else None
    session.close()
    return result

def criar_relatorio(relatorio_data):
    session = SessionLocal()
    relatorio = Relatorio(**relatorio_data)
    session.add(relatorio)
    session.commit()
    session.refresh(relatorio)
    result = relatorio.to_dict()
    session.close()
    return result

def atualizar_relatorio(relatorio_id, relatorio_data):
    session = SessionLocal()
    relatorio = session.query(Relatorio).filter(Relatorio.id == relatorio_id).first()
    if not relatorio:
        session.close()
        return None
    for key, value in relatorio_data.items():
        setattr(relatorio, key, value)
    session.commit()
    session.refresh(relatorio)
    result = relatorio.to_dict()
    session.close()
    return result

def deletar_relatorio(relatorio_id):
    session = SessionLocal()
    relatorio = session.query(Relatorio).filter(Relatorio.id == relatorio_id).first()
    if not relatorio:
        session.close()
        return False
    session.delete(relatorio)
    session.commit()
    session.close()
    return True
