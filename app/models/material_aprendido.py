from app.database import db
from datetime import datetime, timedelta

class MaterialAprendido(db.Model):
    __tablename__ = "materiais_aprendidos"

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    material_type = db.Column(db.String(20), nullable=False)  # pdf, html, video
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"), nullable=False)
    conteudo = db.Column(db.String(255), nullable=False)
    data_aprendizado = db.Column(db.DateTime, default=datetime.utcnow)
    disponivel_de = db.Column(db.DateTime, nullable=False)
    disponivel_ate = db.Column(db.DateTime, nullable=True)

    def __init__(self, aluno_id, conteudo, disciplina_id, titulo, material_type, disponivel_de, disponivel_ate):
        self.aluno_id = aluno_id
        self.conteudo = conteudo
        self.data_aprendizado = datetime.utcnow()
        self.disciplina_id = disciplina_id
        self.titulo = titulo
        self.material_type = material_type
        self.disponivel_de = disponivel_de
        self.disponivel_ate = disponivel_ate

    @property
    def disponivel(self):
        return datetime.utcnow() >= self.disponivel_de

    def __repr__(self):
        return f'<Material {self.titulo} para {self.data_aprendizado.strftime("%d/%m/%Y")}>'