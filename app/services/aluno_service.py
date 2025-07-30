from models.aluno import Aluno

from repositorys.aluno_repository import (
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

def validar_aluno(aluno_data):
    if not aluno_data.get('nome'):
        return "O campo 'nome' é obrigatório."
    if not aluno_data.get('email'):
        return "O campo 'email' é obrigatório."
    if not aluno_data.get('senha'):
        return "O campo 'senha' é obrigatório."
    if not aluno_data.get('turma'):
        return "O campo 'turma' é obrigatório."
    return None

def email_duplicado(email):
    alunos = listar_alunos()
    for aluno in alunos:
        if aluno['email'] == email:
            return True
    return False

def criar_aluno_service(aluno_data):
    erro_validacao = validar_aluno(aluno_data)
    if erro_validacao:
        return {"erro": erro_validacao}

    if email_duplicado(aluno_data['email']):
        return {"erro": "Email já cadastrado."}

    aluno_data = aluno_data.copy()
    aluno_data.pop("confirmacao_senha", None)

    return criar_aluno(aluno_data)

def atualizar_aluno_service(aluno_id, aluno_data):
    aluno_atualizado = atualizar_aluno(aluno_id, aluno_data)
    if not aluno_atualizado:
        return None
    return aluno_atualizado

def deletar_aluno_service(aluno_id):
    return deletar_aluno(aluno_id)
