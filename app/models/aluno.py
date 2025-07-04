from sqlalchemy import Column, Integer, String
from app.database.sias_db import Base
from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class Aluno(Base, BaseModel):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    turma = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)

    grupos = relationship("GrupoAula", secondary="aluno_grupo", back_populates="alunos")
    materiais_visualizados = relationship("MaterialVisualizado", back_populates="aluno")
    respostas_pre_teste = relationship("RespostaPreTeste", back_populates="aluno")
    avaliacoes = relationship("Avaliacao", back_populates="aluno")

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)
    
    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "turma": self.turma
        }