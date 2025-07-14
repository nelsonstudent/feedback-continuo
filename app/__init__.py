# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

# ======== AQUI DEFINIMOS O DB ===================
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    # Inicializa extensão
    db.init_app(app)

    # Registra blueprints (APIs)
    from app.api.report_api import bp as report_bp
    app.register_blueprint(report_bp)

    # Inicia o scheduler em background (sem criar outro app)
    from app.utils.scheduler import scheduler  # noqa: F401

    return app