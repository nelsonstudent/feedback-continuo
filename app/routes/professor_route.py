from flask import Blueprint, request, jsonify
from app.services.professor_service import (
    listar_professores_service,
    criar_professor_service,
    buscar_professor_por_id_service,
    atualizar_professor_service,
    deletar_professor_service
)

professor_bp = Blueprint('professor', __name__, url_prefix='/professores')

@professor_bp.route('/', methods=['GET'])
def listar_professores():
    professores = listar_professores_service()
    return jsonify(professores)

@professor_bp.route('/', methods=['POST'])
def criar_professor():
    data = request.json
    novo_professor = criar_professor_service(data)
    return jsonify(novo_professor), 201

@professor_bp.route('/<int:professor_id>', methods=['GET'])
def buscar_professor(professor_id):
    professor = buscar_professor_por_id_service(professor_id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route('/<int:professor_id>', methods=['PUT'])
def atualizar_professor(professor_id):
    data = request.json
    professor_atualizado = atualizar_professor_service(professor_id, data)
    if professor_atualizado:
        return jsonify(professor_atualizado)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route('/<int:professor_id>', methods=['DELETE'])
def deletar_professor(professor_id):
    sucesso = deletar_professor_service(professor_id)
    if sucesso:
        return jsonify({"mensagem": "Professor deletado com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404
