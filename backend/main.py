from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    nome: str | None = None
    aula: str
    nota: int
    comentario: str

feedbacks = []

@app.post("/feedback")
def receber_feedback(fb: Feedback):
    feedbacks.append(fb)
    return {"msg": "Feedback recebido com sucesso!"}

@app.get("/feedbacks")
def listar_feedbacks():
    return feedbacks
