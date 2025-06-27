from flask import Blueprint, request, jsonify
from app.services.aula_service import (
    listar_aulas_service,
    buscar_aula_por_id_service,
    criar_aula_service,
    atualizar_aula_service,
    deletar_aula_service
)

aula_bp = Blueprint('aula', __name__, url_prefix='/aulas')

@aula_bp.route('/', methods=['GET'])
def listar_aulas():
    aulas = listar_aulas_service()
    return jsonify(aulas)

@aula_bp.route('/<int:aula_id>', methods=['GET'])
def buscar_aula(aula_id):
    aula = buscar_aula_por_id_service(aula_id)
    if aula:
        return jsonify(aula)
    return jsonify({"erro": "Aula não encontrada"}), 404

@aula_bp.route('/', methods=['POST'])
def criar_aula():
    data = request.json
    aula = criar_aula_service(data)
    return jsonify(aula), 201

@aula_bp.route('/<int:aula_id>', methods=['PUT'])
def atualizar_aula(aula_id):
    data = request.json
    aula = atualizar_aula_service(aula_id, data)
    if aula:
        return jsonify(aula)
    return jsonify({"erro": "Aula não encontrada"}), 404

@aula_bp.route('/<int:aula_id>', methods=['DELETE'])
def deletar_aula(aula_id):
    sucesso = deletar_aula_service(aula_id)
    if sucesso:
        return jsonify({"mensagem": "Aula deletada com sucesso"})
    return jsonify({"erro": "Aula não encontrada"}), 404