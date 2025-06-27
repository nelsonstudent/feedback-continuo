from flask import Blueprint, request, jsonify
from app.services.pre_teste_service import (
    listar_pre_testes_service,
    buscar_pre_teste_por_id_service,
    criar_pre_teste_service,
    atualizar_pre_teste_service,
    deletar_pre_teste_service
)

pre_teste_bp = Blueprint('pre_teste', __name__, url_prefix='/pre_testes')

@pre_teste_bp.route('/', methods=['GET'])
def listar_pre_testes():
    pre_testes = listar_pre_testes_service()
    return jsonify(pre_testes)

@pre_teste_bp.route('/<int:pre_teste_id>', methods=['GET'])
def buscar_pre_teste(pre_teste_id):
    pre_teste = buscar_pre_teste_por_id_service(pre_teste_id)
    if pre_teste:
        return jsonify(pre_teste)
    return jsonify({"erro": "Não encontrada"}), 404

@pre_teste_bp.route('/', methods=['POST'])
def criar_pre_teste():
    data = request.json
    nova_pre_teste = criar_pre_teste_service(data)
    return jsonify(nova_pre_teste), 201

@pre_teste_bp.route('/<int:pre_teste_id>', methods=['PUT'])
def atualizar_pre_teste(pre_teste_id):
    data = request.json
    pre_teste_atualizada = atualizar_pre_teste_service(pre_teste_id, data)
    if pre_teste_atualizada:
        return jsonify(pre_teste_atualizada)
    return jsonify({"erro": "Não encontrado"}), 404

@pre_teste_bp.route('/<int:pre_teste_id>', methods=['DELETE'])
def deletar_pre_teste(pre_teste_id):
    sucesso = deletar_pre_teste_service(pre_teste_id)
    if sucesso:
        return jsonify({"mensagem": "Entidade deletada com sucesso"})
    return jsonify({"erro": "Não encontrado"}), 404