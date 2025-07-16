from flask import Blueprint, request, jsonify
from app.services import survey_service

survey_api = Blueprint('survey_api', __name__)

@survey_api.route("/api/surveys", methods=["GET"])
def listar_pesquisas():
    return jsonify(survey_service.listar_ativas())

@survey_api.route("/api/surveys/<int:survey_id>/responder", methods=["POST"])
def responder_pesquisa(survey_id):
    data = request.get_json()
    aluno_id = data.get("aluno_id")
    resposta = data.get("resposta")

    if not aluno_id or not resposta:
        return jsonify({"error": "Campos obrigatórios"}), 400

    result = survey_service.responder_pesquisa(survey_id, aluno_id, resposta)
    if "error" in result:
        return jsonify(result), 400
    return jsonify({"message": "Resposta registrada com sucesso"})