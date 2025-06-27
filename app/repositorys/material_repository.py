from app.models.material import Material
from app.database.sias_db import SessionLocal

def listar_materiais():
    session = SessionLocal()
    materiais = session.query(Material).all()
    result = [material.to_dict() for material in materiais]
    session.close()
    return result

def buscar_material_por_id(material_id):
    session = SessionLocal()
    material = session.query(Material).filter(Material.id == material_id).first()
    result = material.to_dict() if material else None
    session.close()
    return result

def criar_material(material_data):
    session = SessionLocal()
    material = Material(**material_data)
    session.add(material)
    session.commit()
    session.refresh(material)
    result = material.to_dict()
    session.close()
    return result

def atualizar_material(material_id, material_data):
    session = SessionLocal()
    material = session.query(Material).filter(Material.id == material_id).first()
    if not material:
        session.close()
        return None
    for key, value in material_data.items():
        setattr(material, key, value)
    session.commit()
    session.refresh(material)
    result = material.to_dict()
    session.close()
    return result

def deletar_material(material_id):
    session = SessionLocal()
    material = session.query(Material).filter(Material.id == material_id).first()
    if not material:
        session.close()
        return False
    session.delete(material)
    session.commit()
    session.close()
    return True