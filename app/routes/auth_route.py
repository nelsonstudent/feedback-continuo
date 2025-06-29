from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.repositorys.aluno_repository import buscar_aluno_por_email
from app.repositorys.professor_repository import buscar_professor_por_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    user = buscar_aluno_por_email(email)
    tipo = 'aluno'
    if not user or not user.verificar_senha(senha):
        user = buscar_professor_por_email(email)
        tipo = 'professor'
        if not user or not user.verificar_senha(senha):
            return jsonify({"msg": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity={"id": user.id, "tipo": tipo})
    return jsonify(access_token=access_token), 200