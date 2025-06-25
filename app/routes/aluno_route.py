from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.aluno import Aluno

aluno_bp = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['GET'])
def listar_alunos():
    session = SessionLocal()
    alunos = session.query(Aluno).all()
    resultado = [{"id": a.id, "nome": a.nome, "email": a.email, "turma": a.turma} for a in alunos]
    session.close()
    return jsonify(resultado)

@aluno_bp.route('/', methods=['POST'])
def criar_aluno():
    data = request.json
    session = SessionLocal()
    aluno = Aluno(nome=data['nome'], email=data['email'], turma=data['turma'])
    session.add(aluno)
    session.commit()
    session.close()
    return jsonify({"id": aluno.id, "nome": aluno.nome, "email": aluno.email, "turma": aluno.turma}), 201