from app.models.aula_material import AulaMaterial
from app.database.sias_db import SessionLocal

def listar_aula_material():
    session = SessionLocal()
    aula_materials = session.query(AulaMaterial).all()
    result = [aula_material.to_dict() for aula_material in aula_materials]
    session.close()
    return result

def buscar_aula_material_por_id(aula_material_id):
    session = SessionLocal()
    aula_material = session.query(AulaMaterial).filter(AulaMaterial.id == aula_material_id).first()
    result = aula_material.to_dict() if aula_material else None
    session.close()
    return result

def criar_aula_material(aula_material_data):
    session = SessionLocal()
    aula_material = AulaMaterial(**aula_material_data)
    session.add(aula_material)
    session.commit()
    session.refresh(aula_material)
    result = aula_material.to_dict()
    session.close()
    return result

def atualizar_aula_material(aula_material_id, aula_material_data):
    session = SessionLocal()
    aula_material = session.query(AulaMaterial).filter(AulaMaterial.id == aula_material_id).first()
    if not aula_material:
        session.close()
        return None
    for key, value in aula_material_data.items():
        setattr(aula_material, key, value)
    session.commit()
    session.refresh(aula_material)
    result = aula_material.to_dict()
    session.close()
    return result

def deletar_aula_material(aula_material_id):
    session = SessionLocal()
    aula_material = session.query(AulaMaterial).filter(AulaMaterial.id == aula_material_id).first()
    if not aula_material:
        session.close()
        return False
    session.delete(aula_material)
    session.commit()
    session.close()
    return True