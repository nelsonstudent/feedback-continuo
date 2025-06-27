from app.repositorys.material_repository import (
    listar_materiais,
    buscar_material_por_id,
    criar_material,
    atualizar_material,
    deletar_material
)

def listar_materiais_service():
    return listar_materiais()

def buscar_material_por_id_service(material_id):
    material = buscar_material_por_id(material_id)
    if not material:
        return None
    return material

def criar_material_service(material_data):
    return criar_material(material_data)

def atualizar_material_service(material_id, material_data):
    material_atualizado = atualizar_material(material_id, material_data)
    if not material_atualizado:
        return None
    return material_atualizado

def deletar_material_service(material_id):
    return deletar_material(material_id)