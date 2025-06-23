from sqlalchemy import Column, Integer, String
from app.database.sias_db import Base
from sqlalchemy.orm import relationship

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    turma = Column(String, nullable=False)

    grupos = relationship("GrupoAula", secondary="aluno_grupo", back_populates="alunos")
    materiais_visualizados = relationship("MaterialVisualizado", back_populates="aluno")
    respostas_pre_teste = relationship("RespostaPreTeste", back_populates="aluno")
    avaliacoes = relationship("Avaliacao", back_populates="aluno")