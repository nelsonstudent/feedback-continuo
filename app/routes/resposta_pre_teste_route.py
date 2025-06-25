from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.resposta_pre_teste import RespostaPreTeste

resposta_pre_teste_bp = Blueprint(
    'resposta_pre_teste', __name__, url_prefix='/respostas_pre_teste'
)

@resposta_pre_teste_bp.route('/', methods=['GET'])
def listar_respostas_pre_teste():
    session = SessionLocal()
    try:
        respostas = session.query(RespostaPreTeste).all()
        resultado = [
            {
                "id": r.id,
                "aluno_id": r.aluno_id,
                "pre_teste_id": r.pre_teste_id,
                "resposta": r.resposta
            }
            for r in respostas
        ]
        return jsonify(resultado)
    finally:
        session.close()

@resposta_pre_teste_bp.route('/', methods=['POST'])
def criar_resposta_pre_teste():
    data = request.json
    if not all(k in data for k in ('aluno_id', 'pre_teste_id', 'resposta')):
        return jsonify({"erro": "Campos obrigatórios: aluno_id, pre_teste_id, resposta"}), 400

    session = SessionLocal()
    try:
        nova_resposta = RespostaPreTeste(
            aluno_id=data['aluno_id'],
            pre_teste_id=data['pre_teste_id'],
            resposta=data['resposta']
        )
        session.add(nova_resposta)
        session.commit()
        return jsonify({
            "id": nova_resposta.id,
            "aluno_id": nova_resposta.aluno_id,
            "pre_teste_id": nova_resposta.pre_teste_id,
            "resposta": nova_resposta.resposta
        }), 201
    finally:
        session.close()