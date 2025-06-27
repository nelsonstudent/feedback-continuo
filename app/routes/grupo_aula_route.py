from flask import Blueprint, request, jsonify
from app.services.grupo_aula_service import (
    listar_grupos_aula_service,
    buscar_grupo_aula_por_id_service,
    criar_grupo_aula_service,
    atualizar_grupo_aula_service,
    deletar_grupo_aula_service
)

grupo_aula_bp = Blueprint('grupo_aula', __name__, url_prefix='/grupo_aula')

@grupo_aula_bp.route('/', methods=['GET'])
def listar_grupos_aula():
    grupo_aulas = listar_grupos_aula_service()
    return jsonify(grupo_aulas)

@grupo_aula_bp.route('/<int:grupo_aula_id>', methods=['GET'])
def buscar_grupo_aula(grupo_aula_id):
    grupo_aula = buscar_grupo_aula_por_id_service(grupo_aula_id)
    if grupo_aula:
        return jsonify(grupo_aula)
    return jsonify({"erro": "grupo_aula não encontrada"}), 404

@grupo_aula_bp.route('/', methods=['POST'])
def criar_grupo_aula():
    data = request.json
    nova_grupo_aula = criar_grupo_aula_service(data)
    return jsonify(nova_grupo_aula), 201

@grupo_aula_bp.route('/<int:grupo_aula_id>', methods=['PUT'])
def atualizar_grupo_aula(grupo_aula_id):
    data = request.json
    grupo_aula_atualizada = atualizar_grupo_aula_service(grupo_aula_id, data)
    if grupo_aula_atualizada:
        return jsonify(grupo_aula_atualizada)
    return jsonify({"erro": "grupo_aula não encontrada"}), 404

@grupo_aula_bp.route('/<int:grupo_aula_id>', methods=['DELETE'])
def deletar_grupo_aula(grupo_aula_id):
    sucesso = deletar_grupo_aula_service(grupo_aula_id)
    if sucesso:
        return jsonify({"mensagem": "Deletada com sucesso"})
    return jsonify({"erro": "Não encontrada"}), 404