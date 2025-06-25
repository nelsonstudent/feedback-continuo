from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.grupo_aula import GrupoAula

grupo_aula_bp = Blueprint('grupo_aula', __name__, url_prefix='/grupos_aula')

@grupo_aula_bp.route('/', methods=['GET'])
def listar_grupos():
    session = SessionLocal()
    grupos = session.query(GrupoAula).all()
    resultado = [
        {
            "id": g.id,
            "codigo_turma": g.codigo_turma,
            "mentor_id": g.mentor_id
        } for g in grupos
    ]
    session.close()
    return jsonify(resultado)

@grupo_aula_bp.route('/', methods=['POST'])
def criar_grupo():
    data = request.json
    session = SessionLocal()
    grupo = GrupoAula(
        codigo_turma=data['codigo_turma'],
        mentor_id=data['mentor_id']
    )
    session.add(grupo)
    session.commit()
    session.close()
    return jsonify({
        "id": grupo.id,
        "codigo_turma": grupo.codigo_turma,
        "mentor_id": grupo.mentor_id
    }), 201