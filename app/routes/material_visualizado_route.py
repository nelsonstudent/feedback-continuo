from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.material_visualizado import MaterialVisualizado

material_visualizado_bp = Blueprint(
    'material_visualizado', __name__, url_prefix='/materiais_visualizados'
)

@material_visualizado_bp.route('/', methods=['GET'])
def listar_materiais_visualizados():
    session = SessionLocal()
    try:
        materiais_visualizados = session.query(MaterialVisualizado).all()
        resultado = [
            {
                "id": mv.id,
                "aluno_id": mv.aluno_id,
                "material_id": mv.material_id
            }
            for mv in materiais_visualizados
        ]
        return jsonify(resultado)
    finally:
        session.close()

@material_visualizado_bp.route('/', methods=['POST'])
def criar_material_visualizado():
    data = request.json
    if not all(k in data for k in ('aluno_id', 'material_id')):
        return jsonify({"erro": "Campos obrigatórios: aluno_id, material_id"}), 400

    session = SessionLocal()
    try:
        novo_mv = MaterialVisualizado(
            aluno_id=data['aluno_id'],
            material_id=data['material_id']
        )
        session.add(novo_mv)
        session.commit()
        return jsonify({
            "id": novo_mv.id,
            "aluno_id": novo_mv.aluno_id,
            "material_id": novo_mv.material_id
        }), 201
    finally:
        session.close()