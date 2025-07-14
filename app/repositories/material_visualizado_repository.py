from app.models.material_visualizado import MaterialVisualizado
from app.database.sias_db import SessionLocal

def listar_material_visualizado():
    session = SessionLocal()
    materiais_visualizados = session.query(MaterialVisualizado).all()
    result = [material_visualizado.to_dict() for material_visualizado in materiais_visualizados]
    session.close()
    return result

def buscar_material_visualizado_por_id(material_visualizado_id):
    session = SessionLocal()
    material_visualizado = session.query(MaterialVisualizado).filter(MaterialVisualizado.id == material_visualizado_id).first()
    result = material_visualizado.to_dict() if material_visualizado else None
    session.close()
    return result

def criar_material_visualizado(material_visualizado_data):
    session = SessionLocal()
    material_visualizado = MaterialVisualizado(**material_visualizado_data)
    session.add(material_visualizado)
    session.commit()
    session.refresh(material_visualizado)
    result = material_visualizado.to_dict()
    session.close()
    return result

def atualizar_material_visualizado(material_visualizado_id, material_visualizado_data):
    session = SessionLocal()
    material_visualizado = session.query(MaterialVisualizado).filter(MaterialVisualizado.id == material_visualizado_id).first()
    if not material_visualizado:
        session.close()
        return None
    for key, value in material_visualizado_data.items():
        setattr(material_visualizado, key, value)
    session.commit()
    session.refresh(material_visualizado)
    result = material_visualizado.to_dict()
    session.close()
    return result

def deletar_material_visualizado(material_visualizado_id):
    session = SessionLocal()
    material_visualizado = session.query(MaterialVisualizado).filter(MaterialVisualizado.id == material_visualizado_id).first()
    if not material_visualizado:
        session.close()
        return False
    session.delete(material_visualizado)
    session.commit()
    session.close()
    return True
