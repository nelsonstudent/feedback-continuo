from app.repositorys.material_visualizado_repository import (
    listar_material_visualizado,
    buscar_material_visualizado_por_id,
    criar_material_visualizado,
    atualizar_material_visualizado,
    deletar_material_visualizado
)

def listar_material_visualizado_service():
    return listar_material_visualizado()

def buscar_material_visualizado_por_id_service(material_visualizado_id):
    material_visualizado = buscar_material_visualizado_por_id(material_visualizado_id)
    if not material_visualizado:
        return None
    return material_visualizado

def criar_material_visualizado_service(material_visualizado_data):
    return criar_material_visualizado(material_visualizado_data)

def atualizar_material_visualizado_service(material_visualizado_id, material_visualizado_data):
    material_visualizado_atualizado = atualizar_material_visualizado(material_visualizado_id, material_visualizado_data)
    if not material_visualizado_atualizado:
        return None
    return material_visualizado_atualizado

def deletar_material_visualizado_service(material_visualizado_id):
    return deletar_material_visualizado(material_visualizado_id)
