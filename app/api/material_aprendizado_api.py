from flask import jsonify, request
from app.services import material_aprendizado_service
from . import api

@api.route('/materiais_aprendizados', methods=['GET'])
def get_materials(disciplina_id):
    materiais = material_aprendizado_service.get_materials_by_disciplina(disciplina_id)
    return jsonify([{
        "id": m.id,
        "titulo": m.titulo,
        'type': m.material_type,
        "conteudo": m.conteudo,
        "disponivel_de": m.disponivel_de.isoformat(),
        "disponivel_ate": m.disponivel_ate.isoformat() if m.disponivel_ate else None,
        "data_aprendizado": m.data_aprendizado.isoformat() if m.data_aprendizado else None,
        "disponivel": m.disponivel
    } for m in materiais])
    if not materiais:
        return jsonify({"error": "No materials found for this discipline"}), 404
    if not disciplina_id:
        return jsonify({"error": "Disciplina ID is required"}), 400
    aluno_id = request.args.get('aluno_id')
    if not aluno_id:
        return jsonify({"error": "Aluno ID is required"}), 400

    materiais = material_aprendizado_service.get_materials_by_aluno(aluno_id)
    return jsonify(materiais), 200