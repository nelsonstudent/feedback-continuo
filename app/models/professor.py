from sqlalchemy import Column, Integer, String
from app.database.sias_db import Base
from sqlalchemy.orm import relationship

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    materiais = relationship("Material", back_populates="autor")
    pre_testes = relationship("PreTeste", back_populates="autor")
    grupos_mentorados = relationship("GrupoAula", back_populates="mentor")