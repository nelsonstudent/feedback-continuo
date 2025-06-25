from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.pre_teste import PreTeste

pre_teste_bp = Blueprint('pre_teste', __name__, url_prefix='/pre_testes')

@pre_teste_bp.route('/', methods=['GET'])
def listar_pre_testes():
    session = SessionLocal()
    pre_testes = session.query(PreTeste).all()
    resultado = [
        {
            "id": p.id,
            "pergunta": p.pergunta,
            "opcoes": p.opcoes,
            "aula_id": p.aula_id,
            "autor_id": p.autor_id
        } for p in pre_testes
    ]
    session.close()
    return jsonify(resultado)

@pre_teste_bp.route('/', methods=['POST'])
def criar_pre_teste():
    data = request.json
    session = SessionLocal()
    pre_teste = PreTeste(
        pergunta=data['pergunta'],
        opcoes=data.get('opcoes'),
        aula_id=data['aula_id'],
        autor_id=data['autor_id']
    )
    session.add(pre_teste)
    session.commit()
    session.close()
    return jsonify({
        "id": pre_teste.id,
        "pergunta": pre_teste.pergunta,
        "opcoes": pre_teste.opcoes,
        "aula_id": pre_teste.aula_id,
        "autor_id": pre_teste.autor_id
    }), 201