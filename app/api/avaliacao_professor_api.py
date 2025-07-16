from flask import Blueprint, request, jsonify
from app.models import AvaliacaoProfessor
from app.services import avaliacao_professor_service

bp = Blueprint("avaliacao_professor", __name__, url_prefix="/api")

@bp.route("/registrar", methods=["POST"])
def registrar():
    data = request.json
    resultado = avaliacao_professor_service.registrar_avaliacao(data)
    return jsonify({"mensagem": "Avaliação registrada com sucesso", "avaliacao": resultado.id}), 201 if not "error" in resultado else (jsonify(resultado), 400)

@bp.route("/avaliacoes", methods=["POST"])
def criar_avaliacao():
    data = request.json
    resultado = avaliacao_professor_service.criar_avaliacao(data)
    return jsonify(resultado), 201

@bp.route("/avaliacoes", methods=["GET"])
def listar_avaliacoes():
    resultado = avaliacao_professor_service.listar_avaliacoes()
    return jsonify(resultado), 200

@bp.route("/avaliacoes/grupo/<string:grupo>", methods=["GET"])
def obter_avaliacoes_por_grupo(grupo):
    resultado = avaliacao_professor_service.obter_por_grupo(grupo)
    return jsonify(resultado), 200
