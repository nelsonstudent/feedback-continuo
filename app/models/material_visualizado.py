from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class MaterialVisualizado(Base):
    __tablename__ = "materiais_visualizados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    material_id = Column(Integer, ForeignKey("materiais.id"))
    status = Column(String, default="em_andamento")
    data_visualizacao = Column(DateTime)

    aluno = relationship("Aluno", back_populates="materiais_visualizados")
    material = relationship("Material", back_populates="visualizacoes")