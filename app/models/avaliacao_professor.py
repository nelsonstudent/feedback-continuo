from app import db
from datetime import datetime

class AvaliacaoProfessor(db.Model):
    __tablename__ = 'avaliacao_professor'
    
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    aluno_id = db.Column(db.String(50), nullable=False)
    grupo = db.Column(db.String(50), nullable=False)
    avaliacao = db.Column(db.String(255), nullable=False)
    data_avaliacao = db.Column(db.DateTime, default=datetime.utcnow)
    participacao = db.Column(db.Integer, nullable=False)
    dominio_tema = db.Column(db.Integer, nullable=False)
    nota_pre_teste = db.Column(db.Float)  # integração futura
    data_avaliacao = db.Column(db.DateTime, default=datetime.utcnow)