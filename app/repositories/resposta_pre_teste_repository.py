from app.models.resposta_pre_teste import RespostaPreTeste
from app.database.sias_db import SessionLocal

def listar_respostas_pre_teste():
    session = SessionLocal()
    respostas = session.query(RespostaPreTeste).all()
    result = [resposta.to_dict() for resposta in respostas]
    session.close()
    return result

def buscar_resposta_pre_teste_por_id(resposta_id):
    session = SessionLocal()
    resposta = session.query(RespostaPreTeste).filter(RespostaPreTeste.id == resposta_id).first()
    result = resposta.to_dict() if resposta else None
    session.close()
    return result

def criar_resposta_pre_teste(resposta_data):
    session = SessionLocal()
    resposta = RespostaPreTeste(**resposta_data)
    session.add(resposta)
    session.commit()
    session.refresh(resposta)
    result = resposta.to_dict()
    session.close()
    return result

def atualizar_resposta_pre_teste(resposta_id, resposta_data):
    session = SessionLocal()
    resposta = session.query(RespostaPreTeste).filter(RespostaPreTeste.id == resposta_id).first()
    if not resposta:
        session.close()
        return None
    for key, value in resposta_data.items():
        setattr(resposta, key, value)
    session.commit()
    session.refresh(resposta)
    result = resposta.to_dict()
    session.close()
    return result

def deletar_resposta_pre_teste(resposta_id):
    session = SessionLocal()
    resposta = session.query(RespostaPreTeste).filter(RespostaPreTeste.id == resposta_id).first()
    if not resposta:
        session.close()
        return False
    session.delete(resposta)
    session.commit()
    session.close()
    return True