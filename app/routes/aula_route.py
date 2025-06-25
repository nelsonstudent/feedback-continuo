from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.aula import Aula

aula_bp = Blueprint('aula', __name__, url_prefix='/aulas')

@aula_bp.route('/', methods=['GET'])
def listar_aulas():
    session = SessionLocal()
    aulas = session.query(Aula).all()
    resultado = [
        {
            "id": a.id,
            "tema": a.tema,
            "data": a.data,
            "grupo_aula_id": a.grupo_aula_id
        } for a in aulas
    ]
    session.close()
    return jsonify(resultado)

@aula_bp.route('/', methods=['POST'])
def criar_aula():
    data = request.json
    session = SessionLocal()
    aula = Aula(
        tema=data['tema'],
        data=data['data'],
        grupo_aula_id=data['grupo_aula_id']
    )
    session.add(aula)
    session.commit()
    session.close()
    return jsonify({
        "id": aula.id,
        "tema": aula.tema,
        "data": aula.data,
        "grupo_aula_id": aula.grupo_aula_id
    }), 201