from app.repositorys.professor_repository import (
    listar_professores,
    buscar_professor_por_id,
    criar_professor,
    atualizar_professor,
    deletar_professor
)

def listar_professores_service():
    return listar_professores()

def buscar_professor_por_id_service(professor_id):
    professor = buscar_professor_por_id(professor_id)
    if not professor:
        return None
    return professor

def criar_professor_service(professor_data):
    return criar_professor(professor_data)

def atualizar_professor_service(professor_id, professor_data):
    professor_atualizado = atualizar_professor(professor_id, professor_data)
    if not professor_atualizado:
        return None
    return professor_atualizado

def deletar_professor_service(professor_id):
    return deletar_professor(professor_id)