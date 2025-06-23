from app.database.sias_db import Base, SessionLocal, engine
from app.models.professor import Professor
from app.models.aluno import Aluno

Base.metadata.create_all(bind=engine)
session = SessionLocal()