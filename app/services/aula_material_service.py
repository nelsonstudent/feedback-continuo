from app.repositorys.aula_material_repository import (
    listar_aula_material,
    buscar_aula_material_por_id,
    criar_aula_material,
    atualizar_aula_material,
    deletar_aula_material
)

def listar_aula_material_service():
    return listar_aula_material()

def buscar_aula_material_por_id_service(aula_material_id):
    aula_material = buscar_aula_material_por_id(aula_material_id)
    if not aula_material:
        return None
    return aula_material

def criar_aula_material_service(aula_material_data):
    return criar_aula_material(aula_material_data)

def atualizar_aula_material_service(aula_material_id, aula_material_data):
    aula_material_atualizado = atualizar_aula_material(aula_material_id, aula_material_data)
    if not aula_material_atualizado:
        # Aqui poderia levantar uma exceção customizada se desejar
        return None
    return aula_material_atualizado

def deletar_aula_material_service(aula_material_id):
    return deletar_aula_material(aula_material_id)
