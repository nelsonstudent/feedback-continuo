from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.professor import Professor

professor_bp = Blueprint('professor', __name__, url_prefix='/professores')

@professor_bp.route('/', methods=['GET'])
def listar_professores():
    session = SessionLocal()
    professores = session.query(Professor).all()
    resultado = [{"id": p.id, "nome": p.nome, "email": p.email} for p in professores]
    session.close()
    return jsonify(resultado)

@professor_bp.route('/', methods=['POST'])
def criar_professor():
    data = request.json
    session = SessionLocal()
    professor = Professor(nome=data['nome'], email=data['email'])
    session.add(professor)
    session.commit()
    session.close()
    return jsonify({"id": professor.id, "nome": professor.nome, "email": professor.email}), 201