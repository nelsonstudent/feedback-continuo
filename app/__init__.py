from flask import Flask
from app.routes import routes_bp

def create_app(testing=False):
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    if testing:
        app.config["TESTING"] = True
    return app