from sqlalchemy import Column, Integer, String, ForeignKey, Table
from app.database import Base
from sqlalchemy.orm import relationship

aluno_grupo = Table(
    "aluno_grupo", Base.metadata,
    Column("aluno_id", Integer, ForeignKey("alunos.id"), primary_key=True),
    Column("grupo_aula_id", Integer, ForeignKey("grupos_aula.id"), primary_key=True)
)

class GrupoAula(Base):
    __tablename__ = "grupos_aula"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_turma = Column(String, nullable=False, unique=True)
    mentor_id = Column(Integer, ForeignKey("professores.id"))

    mentor = relationship("Professor", back_populates="grupos_mentorados")
    alunos = relationship("Aluno", secondary=aluno_grupo, back_populates="grupos")
    aulas = relationship("Aula", back_populates="grupo_aula")