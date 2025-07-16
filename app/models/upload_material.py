from datetime import datetime
from app import db
class UploadMaterial(db.Model):
    __tablename__ = 'upload_materials'
    
    id = db.Column(db.Integer, primary_key=True)
    nome_arquivo =  db.Column(db.String(255), nullable=False)
    arquivo = db.Column(db.String(512), nullable=True)
    link = db.Column(db.String(512), nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    disponivel_ate = db.Column(db.DateTime, nullable=True)
    ultimo_acesso = db.Column(db.DateTime, nullable=True)

 