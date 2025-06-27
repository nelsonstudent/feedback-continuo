from flask import Blueprint, request, jsonify
from app.services.resposta_pre_teste_service import (
    listar_respostas_pre_teste,
    buscar_resposta_pre_teste_por_id,
    criar_resposta_pre_teste,
    atualizar_resposta_pre_teste_service,
    deletar_resposta_pre_teste_service
)

resposta_pre_teste_bp = Blueprint('resposta_pre_teste', __name__, url_prefix='/respostas_pre_teste')

@resposta_pre_teste_bp.route('/', methods=['GET'])
def listar_respostas_pre_teste():
    respostas_pre_teste = listar_respostas_pre_teste()
    return jsonify(respostas_pre_teste)

@resposta_pre_teste_bp.route('/<int:resposta_pre_teste_id>', methods=['GET'])
def buscar_resposta_pre_teste(resposta_pre_teste_id):
    resposta_pre_teste = buscar_resposta_pre_teste_por_id(resposta_pre_teste_id)
    if resposta_pre_teste:
        return jsonify(resposta_pre_teste)
    return jsonify({"erro": "Não encontrado"}), 404

@resposta_pre_teste_bp.route('/', methods=['POST'])
def criar_resposta_pre_teste():
    data = request.json
    nova_resposta_pre_teste = criar_resposta_pre_teste(data)
    return jsonify(nova_resposta_pre_teste), 201

@resposta_pre_teste_bp.route('/<int:resposta_pre_teste_id>', methods=['PUT'])
def atualizar_resposta_pre_teste(resposta_pre_teste_id):
    data = request.json
    resposta_pre_teste_atualizada = atualizar_resposta_pre_teste_service(resposta_pre_teste_id, data)
    if resposta_pre_teste_atualizada:
        return jsonify(resposta_pre_teste_atualizada)
    return jsonify({"erro": "Não encontrado"}), 404

@resposta_pre_teste_bp.route('/<int:resposta_pre_teste_id>', methods=['DELETE'])
def deletar_resposta_pre_teste(resposta_pre_teste_id):
    sucesso = deletar_resposta_pre_teste_service(resposta_pre_teste_id)
    if sucesso:
        return jsonify({"mensagem": "Deletado com sucesso"})
    return jsonify({"erro": "Não encontrado"}), 404