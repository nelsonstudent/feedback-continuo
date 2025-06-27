from app.models.grupo_aula import GrupoAula
from app.database.sias_db import SessionLocal

def listar_grupos_aula():
    session = SessionLocal()
    grupos = session.query(GrupoAula).all()
    result = [grupo.to_dict() for grupo in grupos]
    session.close()
    return result

def buscar_grupo_aula_por_id(grupo_id):
    session = SessionLocal()
    grupo = session.query(GrupoAula).filter(GrupoAula.id == grupo_id).first()
    result = grupo.to_dict() if grupo else None
    session.close()
    return result

def criar_grupo_aula(grupo_data):
    session = SessionLocal()
    grupo = GrupoAula(**grupo_data)
    session.add(grupo)
    session.commit()
    session.refresh(grupo)
    result = grupo.to_dict()
    session.close()
    return result

def atualizar_grupo_aula(grupo_id, grupo_data):
    session = SessionLocal()
    grupo = session.query(GrupoAula).filter(GrupoAula.id == grupo_id).first()
    if not grupo:
        session.close()
        return None
    for key, value in grupo_data.items():
        setattr(grupo, key, value)
    session.commit()
    session.refresh(grupo)
    result = grupo.to_dict()
    session.close()
    return result

def deletar_grupo_aula(grupo_id):
    session = SessionLocal()
    grupo = session.query(GrupoAula).filter(GrupoAula.id == grupo_id).first()
    if not grupo:
        session.close()
        return False
    session.delete(grupo)
    session.commit()
    session.close()
    return True