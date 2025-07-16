from flask import Flask, app
from app.routes import routes_bp
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
load_dotenv()
import os
from app.api.avaliacao_professor_api import bp as evaluation_bp
app.register_blueprint(evaluation_bp)
def create_app(testing=False):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    jwt = JWTManager(app)
    app.register_blueprint(routes_bp)
    if testing:
        app.config["TESTING"] = True
    return app