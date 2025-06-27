from flask import Blueprint, request, jsonify
from app.services.material_visualizado_service import (
    listar_material_visualizado_service,
    buscar_material_visualizado_por_id_service,
    criar_material_visualizado_service,
    atualizar_material_visualizado_service,
    deletar_material_visualizado_service
)

material_visualizado_bp = Blueprint('material_visualizado', __name__, url_prefix='/material_visualizado')

@material_visualizado_bp.route('/', methods=['GET'])
def listar_material_visualizado():
    material_visualizado = listar_material_visualizado_service()
    return jsonify(material_visualizado)

@material_visualizado_bp.route('/<int:material_visualizado_id>', methods=['GET'])
def buscar_material_visualizado(material_visualizado_id):
    material_visualizado = buscar_material_visualizado_por_id_service(material_visualizado_id)
    if material_visualizado:
        return jsonify(material_visualizado)
    return jsonify({"erro": "Não encontrado"}), 404

@material_visualizado_bp.route('/', methods=['POST'])
def criar_material_visualizado():
    data = request.json
    nova_material_visualizado = criar_material_visualizado_service(data)
    return jsonify(nova_material_visualizado), 201

@material_visualizado_bp.route('/<int:material_visualizado_id>', methods=['PUT'])
def atualizar_material_visualizado(material_visualizado_id):
    data = request.json
    material_visualizado_atualizada = atualizar_material_visualizado_service(material_visualizado_id, data)
    if material_visualizado_atualizada:
        return jsonify(material_visualizado_atualizada)
    return jsonify({"erro": "Não encontrada"}), 404

@material_visualizado_bp.route('/<int:material_visualizado_id>', methods=['DELETE'])
def deletar_material_visualizado(material_visualizado_id):
    sucesso = deletar_material_visualizado_service(material_visualizado_id)
    if sucesso:
        return jsonify({"mensagem": "Deletado com sucesso"})
    return jsonify({"erro": "Não encontrado"}), 404