from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base
from app.models.base import BaseModel
from sqlalchemy.orm import relationship

class Avaliacao(Base, BaseModel):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    nota_escala = Column(Float)
    comentarios = Column(String)
    aula_id = Column(Integer, ForeignKey("aulas.id"))
    aluno_id = Column(Integer, ForeignKey("alunos.id"))

    aula = relationship("Aula", back_populates="avaliacoes")
    aluno = relationship("Aluno", back_populates="avaliacoes")