from app.repositorys.aluno_repository import (
    listar_alunos,
    buscar_aluno_por_id,
    criar_aluno,
    atualizar_aluno,
    deletar_aluno
)

def listar_alunos_service():
    return listar_alunos()

def buscar_aluno_por_id_service(aluno_id):
    aluno = buscar_aluno_por_id(aluno_id)
    if not aluno:
        return None
    return aluno

def criar_aluno_service(aluno_data):
    return criar_aluno(aluno_data)

def atualizar_aluno_service(aluno_id, aluno_data):
    aluno_atualizado = atualizar_aluno(aluno_id, aluno_data)
    if not aluno_atualizado:
        return None
    return aluno_atualizado

def deletar_aluno_service(aluno_id):
    return deletar_aluno(aluno_id)