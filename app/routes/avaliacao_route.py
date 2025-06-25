from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.avaliacao import Avaliacao

avaliacao_bp = Blueprint('avaliacao', __name__, url_prefix='/avaliacoes')

@avaliacao_bp.route('/', methods=['GET'])
def listar_avaliacoes():
    session = SessionLocal()
    avaliacoes = session.query(Avaliacao).all()
    resultado = [
        {
            "id": a.id,
            "tipo": a.tipo,
            "nota_escala": a.nota_escala,
            "comentarios": a.comentarios,
            "aula_id": a.aula_id,
            "aluno_id": a.aluno_id
        } for a in avaliacoes
    ]
    session.close()
    return jsonify(resultado)

@avaliacao_bp.route('/', methods=['POST'])
def criar_avaliacao():
    data = request.json
    session = SessionLocal()
    avaliacao = Avaliacao(
        tipo=data['tipo'],
        nota_escala=data.get('nota_escala'),
        comentarios=data.get('comentarios'),
        aula_id=data['aula_id'],
        aluno_id=data['aluno_id']
    )
    session.add(avaliacao)
    session.commit()
    session.close()
    return jsonify({
        "id": avaliacao.id,
        "tipo": avaliacao.tipo,
        "nota_escala": avaliacao.nota_escala,
        "comentarios": avaliacao.comentarios,
        "aula_id": avaliacao.aula_id,
        "aluno_id": avaliacao.aluno_id
    }), 201