from app.repositorys.grupo_aula_repository import (
    listar_grupos_aula,
    buscar_grupo_aula_por_id,
    criar_grupo_aula,
    atualizar_grupo_aula,
    deletar_grupo_aula
)

def listar_grupos_aula_service():
    return listar_grupos_aula()

def buscar_grupo_aula_por_id_service(grupo_aula_id):
    grupo_aula = buscar_grupo_aula_por_id(grupo_aula_id)
    if not grupo_aula:
        return None
    return grupo_aula

def criar_grupo_aula_service(grupo_aula_data):
    return criar_grupo_aula(grupo_aula_data)

def atualizar_grupo_aula_service(grupo_aula_id, grupo_aula_data):
    grupo_aula_atualizado = atualizar_grupo_aula(grupo_aula_id, grupo_aula_data)
    if not grupo_aula_atualizado:
        return None
    return grupo_aula_atualizado

def deletar_grupo_aula_service(grupo_aula_id):
    return deletar_grupo_aula(grupo_aula_id)