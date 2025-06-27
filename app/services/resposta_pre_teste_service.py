from app.repositorys.resposta_pre_teste_repository import (
    listar_respostas_pre_teste,
    buscar_resposta_pre_teste_por_id,
    criar_resposta_pre_teste,
    atualizar_resposta_pre_teste,
    deletar_resposta_pre_teste
)

def listar_respostas_pre_teste():
    return listar_respostas_pre_teste()

def buscar_reposta_pre_teste_por_id_service(reposta_pre_teste_id):
    reposta_pre_teste = buscar_resposta_pre_teste_por_id(reposta_pre_teste_id)
    if not reposta_pre_teste:
        return None
    return reposta_pre_teste

def criar_reposta_pre_teste_service(reposta_pre_teste_data):
    return criar_resposta_pre_teste(reposta_pre_teste_data)

def atualizar_resposta_pre_teste_service(reposta_pre_teste_id, reposta_pre_teste_data):
    reposta_pre_teste_atualizada = atualizar_resposta_pre_teste(reposta_pre_teste_id, reposta_pre_teste_data)
    if not reposta_pre_teste_atualizada:
        return None
    return reposta_pre_teste_atualizada

def deletar_resposta_pre_teste_service(reposta_pre_teste_id):
    return deletar_resposta_pre_teste(reposta_pre_teste_id)