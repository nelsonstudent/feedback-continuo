from sqlalchemy import Column, Integer, String
from app.database.sias_db import Base

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)