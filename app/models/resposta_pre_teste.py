from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class RespostaPreTeste(Base):
    __tablename__ = "respostas_pre_teste"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    pre_teste_id = Column(Integer, ForeignKey("pre_testes.id"))
    resposta = Column(String, nullable=False)
    data_resposta = Column(DateTime)

    aluno = relationship("Aluno", back_populates="respostas_pre_teste")
    pre_teste = relationship("PreTeste", back_populates="respostas")