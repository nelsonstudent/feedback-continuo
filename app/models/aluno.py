from sqlalchemy import Column, Integer, String
from app.database.sias_db import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    turma = Column(String, nullable=False)