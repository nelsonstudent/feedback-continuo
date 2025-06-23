from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class PreTeste(Base):
    __tablename__ = "pre_testes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pergunta = Column(String, nullable=False)
    opcoes = Column(String)
    aula_id = Column(Integer, ForeignKey("aulas.id"))
    autor_id = Column(Integer, ForeignKey("professores.id"))

    aula = relationship("Aula", back_populates="pre_testes")
    autor = relationship("Professor", back_populates="pre_testes")
    respostas = relationship("RespostaPreTeste", back_populates="pre_teste")