from app.repositorys.relatorio_repository import (
    listar_relatorios,
    buscar_relatorio_por_id,
    criar_relatorio,
    atualizar_relatorio,
    deletar_relatorio
)

def listar_relatorios_service():
    return listar_relatorios()

def buscar_relatorio_por_id_service(relatorio_id):
    relatorio = buscar_relatorio_por_id(relatorio_id)
    if not relatorio:
        return None
    return relatorio

def criar_relatorio_service(relatorio_data):
    return criar_relatorio(relatorio_data)

def atualizar_relatorio_service(relatorio_id, relatorio_data):
    relatorio_atualizado = atualizar_relatorio(relatorio_id, relatorio_data)
    if not relatorio_atualizado:
        return None
    return relatorio_atualizado

def deletar_relatorio_service(relatorio_id):
    return deletar_relatorio(relatorio_id)