from flask import jsonify, Blueprint
from app import db
from app.services import materiais_concluidos_service, material_service

bp = Blueprint('materiais_concluidos', __name__)

@bp.route('/<int:id>/materiais_concluidos', methods=['POST'])
def marcar_concluido(id):
    resultado, status = materiais_concluidos_service.marcar_concluido(id)
    return jsonify(resultado), status

@bp.route('/materiais_concluidos', methods=['GET'])
def listar_materiais_concluidos():
    resultado, status = materiais_concluidos_service.listar_materiais_concluidos()
    return jsonify([{
        "id": m.id,
        "titulo": m.titulo,
        'type': m.material_type,
        "conteudo": m.conteudo,
        "disponivel_de": m.disponivel_de.isoformat(),
        "disponivel_ate": m.disponivel_ate.isoformat() if m.disponivel_ate else None,
        "data_aprendizado": m.data_aprendizado.isoformat() if m.data_aprendizado else None,
        "disponivel": m.disponivel,
        "concluido": m.concluido
    } for m in resultado]), status