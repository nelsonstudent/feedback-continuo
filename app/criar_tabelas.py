from flask.cli import locate_app
from app import criar_tabelas, db
from app.models.material_aprendido import MaterialAprendido
from app.services.material_aprendizagem_service import MaterialAprendizadoService
from app.api.material_aprendizado_api import api
from flask import Flask

app = Flask(__name__)

def criar_tabelas():
    app = locate_app()
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)