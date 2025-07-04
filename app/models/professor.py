from sqlalchemy import Column, Integer, String
from app.database.sias_db import Base
from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class Professor(Base, BaseModel):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha_hash = Column(String, nullable=False)

    materiais = relationship("Material", back_populates="autor")
    pre_testes = relationship("PreTeste", back_populates="autor")
    grupos_mentorados = relationship("GrupoAula", back_populates="mentor")
    
    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)
    
    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }    