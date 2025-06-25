from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.relatorio import Relatorio

relatorio_bp = Blueprint('relatorio', __name__, url_prefix='/relatorios')

@relatorio_bp.route('/', methods=['GET'])
def listar_relatorios():
    session = SessionLocal()
    relatorios = session.query(Relatorio).all()
    resultado = [
        {
            "id": r.id,
            "tipo": r.tipo,
            "nota_escala": r.nota_escala,
            "comentarios": r.comentarios,
            "aula_id": r.aula_id,
            "aluno_id": r.aluno_id
        } for r in relatorios
    ]
    session.close()
    return jsonify(resultado)

@relatorio_bp.route('/', methods=['POST'])
def criar_relatorio():
    data = request.json
    session = SessionLocal()
    relatorio = Relatorio(
        tipo=data.get('tipo'),
        nota_escala=data.get('nota_escala'),
        comentarios=data.get('comentarios'),
        aula_id=data['aula_id'],
        aluno_id=data['aluno_id']
    )
    session.add(relatorio)
    session.commit()
    session.close()
    return jsonify({
        "id": relatorio.id,
        "tipo": relatorio.tipo,
        "nota_escala": relatorio.nota_escala,
        "comentarios": relatorio.comentarios,
        "aula_id": relatorio.aula_id,
        "aluno_id": relatorio.aluno_id
    }), 201