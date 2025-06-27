from app.models.pre_teste import PreTeste
from app.database.sias_db import SessionLocal

def listar_pre_testes():
    session = SessionLocal()
    pre_testes = session.query(PreTeste).all()
    result = [pre_teste.to_dict() for pre_teste in pre_testes]
    session.close()
    return result

def buscar_pre_teste_por_id(pre_teste_id):
    session = SessionLocal()
    pre_teste = session.query(PreTeste).filter(PreTeste.id == pre_teste_id).first()
    result = pre_teste.to_dict() if pre_teste else None
    session.close()
    return result

def criar_pre_teste(pre_teste_data):
    session = SessionLocal()
    pre_teste = PreTeste(**pre_teste_data)
    session.add(pre_teste)
    session.commit()
    session.refresh(pre_teste)
    result = pre_teste.to_dict()
    session.close()
    return result

def atualizar_pre_teste(pre_teste_id, pre_teste_data):
    session = SessionLocal()
    pre_teste = session.query(PreTeste).filter(PreTeste.id == pre_teste_id).first()
    if not pre_teste:
        session.close()
        return None
    for key, value in pre_teste_data.items():
        setattr(pre_teste, key, value)
    session.commit()
    session.refresh(pre_teste)
    result = pre_teste.to_dict()
    session.close()
    return result

def deletar_pre_teste(pre_teste_id):
    session = SessionLocal()
    pre_teste = session.query(PreTeste).filter(PreTeste.id == pre_teste_id).first()
    if not pre_teste:
        session.close()
        return False
    session.delete(pre_teste)
    session.commit()
    session.close()
    return True