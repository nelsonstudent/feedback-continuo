from flask import Blueprint, request, jsonify
from app.services.avaliacao_service import (
    listar_avaliacoes_service,
    buscar_avaliacao_por_id_service,
    criar_avaliacao_service,
    atualizar_avaliacao_service,
    deletar_avaliacao_service
)

avaliacao_bp = Blueprint('avaliacao', __name__, url_prefix='/avaliacoes')

@avaliacao_bp.route('/', methods=['GET'])
def listar_avaliacoes():
    avaliacoes = listar_avaliacoes_service()
    return jsonify(avaliacoes)

@avaliacao_bp.route('/<int:avaliacao_id>', methods=['GET'])
def buscar_avaliacao(avaliacao_id):
    avaliacao = buscar_avaliacao_por_id_service(avaliacao_id)
    if avaliacao:
        return jsonify(avaliacao)
    return jsonify({"erro": "avaliacao não encontrada"}), 404

@avaliacao_bp.route('/', methods=['POST'])
def criar_avaliacao():
    data = request.json
    nova_avaliacao = criar_avaliacao_service(data)
    return jsonify(nova_avaliacao), 201

@avaliacao_bp.route('/<int:avaliacao_id>', methods=['PUT'])
def atualizar_avaliacao(avaliacao_id):
    data = request.json
    avaliacao_atualizada = atualizar_avaliacao_service(avaliacao_id, data)
    if avaliacao_atualizada:
        return jsonify(avaliacao_atualizada)
    return jsonify({"erro": "avaliacao não encontrada"}), 404

@avaliacao_bp.route('/<int:avaliacao_id>', methods=['DELETE'])
def deletar_avaliacao(avaliacao_id):
    sucesso = deletar_avaliacao_service(avaliacao_id)
    if sucesso:
        return jsonify({"mensagem": "avaliacao deletada com sucesso"})
    return jsonify({"erro": "avaliacao não encontrada"}), 404