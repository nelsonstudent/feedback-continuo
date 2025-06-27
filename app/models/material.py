from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from app.models.aula_material import aula_material

class Material(Base, BaseModel):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    anexo = Column(String)
    data_publicacao = Column(DateTime)
    autor_id = Column(Integer, ForeignKey("professores.id"))

    autor = relationship("Professor", back_populates="materiais")
    visualizacoes = relationship("MaterialVisualizado", back_populates="material")
    aulas = relationship("Aula", secondary=aula_material, back_populates="materiais")