# app/api/report_api.py
from flask import Blueprint, jsonify, abort
from app.services.report_service import gerar_relatorio

bp = Blueprint('reports', __name__, url_prefix='/api/reports')

@bp.route('/<aula_id>/reprocess', methods=['POST'])
def reprocessar(aula_id):
    try:
        url = gerar_relatorio(aula_id)
        return jsonify({'url': url}), 200
    except PermissionError as pe:
        abort(403, str(pe))
    except Exception as e:
        abort(500, str(e))
