from sqlalchemy import Column, Integer, String
from database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=True)
    aula = Column(String, index=True)
    nota = Column(Integer)
    comentario = Column(String)
