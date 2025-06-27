from flask import Blueprint, request, jsonify
from app.services.relatorio_service import (
    listar_relatorios_service,
    buscar_relatorio_por_id_service,
    criar_relatorio_service,
    atualizar_relatorio_service,
    deletar_relatorio_service
)

relatorio_bp = Blueprint('relatorio', __name__, url_prefix='/relatorios')

@relatorio_bp.route('/', methods=['GET'])
def listar_relatorios():
    relatorios = listar_relatorios_service()
    return jsonify(relatorios)

@relatorio_bp.route('/<int:relatorio_id>', methods=['GET'])
def buscar_relatorio(relatorio_id):
    relatorio = buscar_relatorio_por_id_service(relatorio_id)
    if relatorio:
        return jsonify(relatorio)
    return jsonify({"erro": "Relatório não encontrado"}), 404

@relatorio_bp.route('/', methods=['POST'])
def criar_relatorio():
    data = request.json
    nova_relatorio = criar_relatorio_service(data)
    return jsonify(nova_relatorio), 201

@relatorio_bp.route('/<int:relatorio_id>', methods=['PUT'])
def atualizar_relatorio(relatorio_id):
    data = request.json
    relatorio_atualizada = atualizar_relatorio_service(relatorio_id, data)
    if relatorio_atualizada:
        return jsonify(relatorio_atualizada)
    return jsonify({"erro": "Relatório não encontrado"}), 404

@relatorio_bp.route('/<int:relatorio_id>', methods=['DELETE'])
def deletar_relatorio(relatorio_id):
    sucesso = deletar_relatorio_service(relatorio_id)
    if sucesso:
        return jsonify({"mensagem": "Entidade deletada com sucesso"})
    return jsonify({"erro": "Relatório não encontrado"}), 404