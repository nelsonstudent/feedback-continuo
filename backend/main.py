from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic schema
class FeedbackSchema(BaseModel):
    nome: str | None = None
    aula: str
    nota: int
    comentario: str

    class Config:
        orm_mode = True

# Dependency para pegar a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/feedback")
def criar_feedback(fb: FeedbackSchema, db: Session = Depends(get_db)):
    feedback = models.Feedback(**fb.dict())
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

@app.get("/feedbacks")
def listar_feedbacks(db: Session = Depends(get_db)):
    return db.query(models.Feedback).all()
