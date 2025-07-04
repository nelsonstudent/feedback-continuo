from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.aluno_service import (
    listar_alunos_service,
    buscar_aluno_por_id_service,
    criar_aluno_service,
    atualizar_aluno_service,
    deletar_aluno_service
)

aluno_bp = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['GET'], endpoint='listar_alunos')
@jwt_required()
def listar_alunos():
    alunos = listar_alunos_service()
    return jsonify(alunos)

@aluno_bp.route('/<int:aluno_id>', methods=['GET'], endpoint='buscar_aluno')
@jwt_required()
def buscar_aluno(aluno_id):
    print("DEBUG: /alunos/ endpoint chamado")
    aluno = buscar_aluno_por_id_service(aluno_id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "aluno não encontrado"}), 404

@aluno_bp.route('/', methods=['POST'], endpoint='criar_aluno')
def criar_aluno():
    data = request.json
    nova_aluno = criar_aluno_service(data)
    return jsonify(nova_aluno.to_dict()), 201

@aluno_bp.route('/<int:aluno_id>', methods=['PUT'], endpoint='atualizar_aluno')
@jwt_required()
def atualizar_aluno(aluno_id):
    data = request.json
    aluno_atualizada = atualizar_aluno_service(aluno_id, data)
    if aluno_atualizada:
        return jsonify(aluno_atualizada)
    return jsonify({"erro": "aluno não encontrado"}), 404

@aluno_bp.route('/<int:aluno_id>', methods=['DELETE'], endpoint='deletar_aluno')
@jwt_required()
def deletar_aluno(aluno_id):
    sucesso = deletar_aluno_service(aluno_id)
    if sucesso:
        return jsonify({"mensagem": "aluno deletado com sucesso"})
    return jsonify({"erro": "aluno não encontrada"}), 404
