from flask import Blueprint, request, jsonify
from app.services.material_service import (
    listar_materiais_service,
    buscar_material_por_id_service,
    criar_material_service,
    atualizar_material_service,
    deletar_material_service
)

material_bp = Blueprint('material', __name__, url_prefix='/materiais')

@material_bp.route('/', methods=['GET'])
def listar_materiais():
    materiais = listar_materiais_service()
    return jsonify(materiais)

@material_bp.route('/<int:material_id>', methods=['GET'])
def buscar_material(material_id):
    material = buscar_material_por_id_service(material_id)
    if material:
        return jsonify(material)
    return jsonify({"erro": "material não encontrada"}), 404

@material_bp.route('/', methods=['POST'])
def criar_material():
    data = request.json
    nova_material = criar_material_service(data)
    return jsonify(nova_material), 201

@material_bp.route('/<int:material_id>', methods=['PUT'])
def atualizar_material(material_id):
    data = request.json
    material_atualizada = atualizar_material_service(material_id, data)
    if material_atualizada:
        return jsonify(material_atualizada)
    return jsonify({"erro": "Material não encontrada"}), 404

@material_bp.route('/<int:material_id>', methods=['DELETE'])
def deletar_material(material_id):
    sucesso = deletar_material_service(material_id)
    if sucesso:
        return jsonify({"mensagem": "Material deletada com sucesso"})
    return jsonify({"erro": "Material não encontrada"}), 404