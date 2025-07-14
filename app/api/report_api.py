# app/api/report_api.py
from flask import Blueprint

bp = Blueprint('report', __name__)

@bp.route('/hello')
def hello():
    return "Hello from report_api"
