from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tema = Column(String, nullable=False)
    data = Column(DateTime, nullable=False)
    grupo_aula_id = Column(Integer, ForeignKey("grupos_aula.id"))

    grupo_aula = relationship("GrupoAula", back_populates="aulas")
    materiais = relationship("Material", secondary="aula_material", back_populates="aulas")
    pre_testes = relationship("PreTeste", back_populates="aula")
    avaliacoes = relationship("Avaliacao", back_populates="aula")
    relatorios = relationship("Relatorio", back_populates="aula")