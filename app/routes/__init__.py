from flask import Blueprint
from .aluno_route import aluno_bp
from .professor_route import professor_bp
from .material_route import material_bp
from .aula_route import aula_bp
from .grupo_aula_route import grupo_aula_bp
from .pre_teste_route import pre_teste_bp
from .avaliacao_route import avaliacao_bp
from .relatorio_route import relatorio_bp
from .resposta_pre_teste_route import resposta_pre_teste_bp
from .material_visualizado_route import material_visualizado_bp
from .auth_route import auth_bp

routes_bp = Blueprint('routes', __name__)

routes_bp.register_blueprint(aluno_bp)
routes_bp.register_blueprint(professor_bp)
routes_bp.register_blueprint(material_bp)
routes_bp.register_blueprint(aula_bp)
routes_bp.register_blueprint(grupo_aula_bp)
routes_bp.register_blueprint(pre_teste_bp)
routes_bp.register_blueprint(avaliacao_bp)
routes_bp.register_blueprint(relatorio_bp)
routes_bp.register_blueprint(resposta_pre_teste_bp)
routes_bp.register_blueprint(material_visualizado_bp)
routes_bp.register_blueprint(auth_bp)