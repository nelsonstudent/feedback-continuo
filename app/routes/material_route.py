from flask import Blueprint, request, jsonify
from app.database import SessionLocal
from app.models.material import Material

material_bp = Blueprint('material', __name__, url_prefix='/materiais')

@material_bp.route('/', methods=['GET'])
def listar_materiais():
    session = SessionLocal()
    materiais = session.query(Material).all()
    resultado = [
        {
            "id": m.id,
            "titulo": m.titulo,
            "tipo": m.tipo,
            "anexo": m.anexo,
            "data_publicacao": m.data_publicacao,
            "autor_id": m.autor_id
        } for m in materiais
    ]
    session.close()
    return jsonify(resultado)

@material_bp.route('/', methods=['POST'])
def criar_material():
    data = request.json
    session = SessionLocal()
    material = Material(
        titulo=data['titulo'],
        tipo=data['tipo'],
        anexo=data.get('anexo'),
        data_publicacao=data.get('data_publicacao'),
        autor_id=data['autor_id']
    )
    session.add(material)
    session.commit()
    session.close()
    return jsonify({
        "id": material.id,
        "titulo": material.titulo,
        "tipo": material.tipo,
        "anexo": material.anexo,
        "data_publicacao": material.data_publicacao,
        "autor_id": material.autor_id
    }), 201