from app.models.avaliacao import Avaliacao
from app.database.sias_db import SessionLocal

def listar_avaliacoes():
    session = SessionLocal()
    avaliacoes = session.query(Avaliacao).all()
    result = [avaliacao.to_dict() for avaliacao in avaliacoes]
    session.close()
    return result

def buscar_avaliacao_por_id(avaliacao_id):
    session = SessionLocal()
    avaliacao = session.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()
    result = avaliacao.to_dict() if avaliacao else None
    session.close()
    return result

def criar_avaliacao(avaliacao_data):
    session = SessionLocal()
    avaliacao = Avaliacao(**avaliacao_data)
    session.add(avaliacao)
    session.commit()
    session.refresh(avaliacao)
    result = avaliacao.to_dict()
    session.close()
    return result

def atualizar_avaliacao(avaliacao_id, avaliacao_data):
    session = SessionLocal()
    avaliacao = session.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()
    if not avaliacao:
        session.close()
        return None
    for key, value in avaliacao_data.items():
        setattr(avaliacao, key, value)
    session.commit()
    session.refresh(avaliacao)
    result = avaliacao.to_dict()
    session.close()
    return result

def deletar_avaliacao(avaliacao_id):
    session = SessionLocal()
    avaliacao = session.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()
    if not avaliacao:
        session.close()
        return False
    session.delete(avaliacao)
    session.commit()
    session.close()
    return True