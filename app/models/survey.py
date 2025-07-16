from app import db
from datetime import datetime

class Survey(db.Model):
    __tablename__ = 'surveys'
    
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, onupdate=datetime.utcnow)
    opcoes = db.Column(db.String(255), nullable=False)  # Ex: "Sim,Não,Mais ou menos"
    ativo = db.Column(db.Boolean, default=True)
    respostas = db.relationship('Resposta', backref='survey', lazy=True)
class Resposta(db.Model):
    __tablename__ = 'respostas'
    
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'), nullable=False)
    aluno_id = db.Column(db.String(50), nullable=False)  # Pode ser RA, e-mail ou ID do aluno
    resposta = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('survey_id', 'aluno_id', name='uq_resposta_unica'),)
