from flask import Flask
from app.routes import routes_bp
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
load_dotenv()
import os

def create_app(testing=False):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    jwt = JWTManager(app)
    app.register_blueprint(routes_bp)
    if testing:
        app.config["TESTING"] = True
    return app