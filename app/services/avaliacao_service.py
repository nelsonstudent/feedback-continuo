from app.repositorys.avaliacao_repository import (
    listar_avaliacoes,
    buscar_avaliacao_por_id,
    criar_avaliacao,
    atualizar_avaliacao,
    deletar_avaliacao
)

def listar_avaliacoes_service():
    return listar_avaliacoes()

def buscar_avaliacao_por_id_service(avaliacao_id):
    avaliacao = buscar_avaliacao_por_id(avaliacao_id)
    if not avaliacao:
        return None
    return avaliacao

def criar_avaliacao_service(avaliacao_data):
    return criar_avaliacao(avaliacao_data)

def atualizar_avaliacao_service(avaliacao_id, avaliacao_data):
    avaliacao_atualizada = atualizar_avaliacao(avaliacao_id, avaliacao_data)
    if not avaliacao_atualizada:
        return None
    return avaliacao_atualizada

def deletar_avaliacao_service(avaliacao_id):
    return deletar_avaliacao(avaliacao_id)