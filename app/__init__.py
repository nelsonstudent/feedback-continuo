from flask import Flask
from flask_cors import CORS
from routes import routes_bp
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

def create_app(testing=False):
    app = Flask(__name__)

    # CORS global cobre todas as rotas e blueprints
    CORS(
        app,
        origins=["http://localhost:3000", "http://sias-frontend:3000"],
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    )

    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    jwt = JWTManager(app)
    app.register_blueprint(routes_bp)
    if testing:
        app.config["TESTING"] = True
    return app