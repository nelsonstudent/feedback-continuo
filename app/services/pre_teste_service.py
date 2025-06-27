from app.repositorys.pre_teste_repository import (
    listar_pre_testes,
    buscar_pre_teste_por_id,
    criar_pre_teste,
    atualizar_pre_teste,
    deletar_pre_teste
)

def listar_pre_testes_service():
    return listar_pre_testes()

def buscar_pre_teste_por_id_service(pre_teste_id):
    pre_teste = buscar_pre_teste_por_id(pre_teste_id)
    if not pre_teste:
        return None
    return pre_teste

def criar_pre_teste_service(pre_teste_data):
    return criar_pre_teste(pre_teste_data)

def atualizar_pre_teste_service(pre_teste_id, pre_teste_data):
    pre_teste_atualizado = atualizar_pre_teste(pre_teste_id, pre_teste_data)
    if not pre_teste_atualizado:
        return None
    return pre_teste_atualizado

def deletar_pre_teste_service(pre_teste_id):
    return deletar_pre_teste(pre_teste_id)