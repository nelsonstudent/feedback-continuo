from app.repositorys.aula_repository import (
    listar_aulas,
    buscar_aula_por_id,
    criar_aula,
    atualizar_aula,
    deletar_aula
)

def listar_aulas_service():
    return listar_aulas()

def buscar_aula_por_id_service(aula_id):
    aula = buscar_aula_por_id(aula_id)
    if not aula:
        return None
    return aula

def criar_aula_service(aula_data):
    return criar_aula(aula_data)

def atualizar_aula_service(aula_id, aula_data):
    aula_atualizada = atualizar_aula(aula_id, aula_data)
    if not aula_atualizada:
        # Aqui poderia levantar uma exceção customizada se desejar
        return None
    return aula_atualizada

def deletar_aula_service(aula_id):
    return deletar_aula(aula_id)
