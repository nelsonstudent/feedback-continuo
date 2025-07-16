from app.repositories.materiais_concluidos_repo import marcar_concluido, list_unaccessed, list_materials, list_unaccessed_by_aluno
from flask import jsonify, request
from app import db
from app.models.materiais_concluidos import MateriaisConcluidos
from . import api
@api.route('/materiais_concluidos', methods=['POST'])

def marcar_concluido(material_id, aluno_id):
    data = request.get_json()
    material_id = marcar_concluido(material_id, aluno_id)
    if not material_id:
        return jsonify({"error": "Material ID is required"}), 400
    if not aluno_id:
        return jsonify({"error": "Aluno ID is required"}), 400
    material_id = data.get('material_id')
    if not material_id:
        return jsonify({"error": "Material ID is required"}), 400
    aluno_id = data.get('aluno_id')

    if not aluno_id:
        return jsonify({"error": "Aluno ID is required"}), 400
    material = marcar_concluido(material_id, aluno_id)
    if not material:
        return jsonify({"error": "Material not found or already marked as completed"}), 404

    return jsonify({"message": "Material marked as completed", "material": material.id}), 200
def listar_concluidos():
    aluno_id = request.args.get('aluno_id')
    if not aluno_id:
        return jsonify({"error": "Aluno ID is required"}), 400
    materiais = listar_concluidos(aluno_id)
    return jsonify({"materiais": [m.id for m in materiais]}), 200
def listar_materiais():
    disciplina_id = request.args.get('disciplina_id')
    if not disciplina_id:
        return jsonify({"error": "É necessário fornecer o ID da disciplina"}), 400
    materiais = listar_materiais(disciplina_id)
    if not materiais:
        return jsonify({"error": "Nenhum material encontrado para esta disciplina"}), 404
    return jsonify([{
        "id": m.id,
        "titulo": m.titulo,
        'type': m.material_type,
        "conteudo": m.conteudo,
        "disponivel_de": m.disponivel_de.isoformat(),
        "disponivel_ate": m.disponivel_ate.isoformat() if m.disponivel_ate else None,
        "data_aprendizado": m.data_aprendizado.isoformat() if m.data_aprendizado else None,
        "disponivel": m.disponivel
    } for m in materiais]), 200
def listar_unaccessed():
    aluno_id = request.args.get('aluno_id')
    if not aluno_id:
        return jsonify({"error": "É necessário fornecer o ID do aluno"}), 400
    materiais = list_unaccessed(aluno_id)
    return jsonify([{
        "id": m.id,
        "titulo": m.titulo,
        'type': m.material_type,
        "conteudo": m.conteudo,
        "disponivel_de": m.disponivel_de.isoformat(),
        "disponivel_ate": m.disponivel_ate.isoformat() if m.disponivel_ate else None,
        "data_aprendizado": m.data_aprendizado.isoformat() if m.data_aprendizado else None,
        "disponivel": m.disponivel
    } for m in materiais]), 200
