from app.repositories import survey_repo
from app.models.survey import Survey, Resposta
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app import db

def responder_pesquisa(survey_id, aluno_id, resposta):
    if survey_repo.aluno_ja_respondeu(survey_id, aluno_id):
        return {"error": "Aluno já respondeu a esta pesquisa."}, 400
    
    try:
        nova_resposta = survey_repo.salvar_resposta(survey_id, aluno_id, resposta)
        if nova_resposta:
            return {"message": "Resposta salva com sucesso.", "resposta": nova_resposta}, 201
        else:
            return {"error": "Erro ao salvar a resposta."}, 500
    except IntegrityError:
        db.session.rollback()
        return {"error": "Erro de integridade ao salvar a resposta."}, 500
def criar_pesquisa(pergunta, opcoes):
    if not pergunta or not opcoes:
        return {"error": "Pergunta e opções são obrigatórias."}, 400
    
    try:
        nova_pesquisa = survey_repo.criar_pesquisa(pergunta, opcoes)
        if nova_pesquisa:
            return {"message": "Pesquisa criada com sucesso.", "pesquisa": nova_pesquisa}, 201
        else:
            return {"error": "Erro ao criar a pesquisa."}, 500
    except IntegrityError:
        db.session.rollback()
        return {"error": "Erro de integridade ao criar a pesquisa."}, 500
def listar_pesquisas_ativas():
    pesquisas = survey_repo.listar_pesquisas_ativas()
    return [
        {
            "id": pesquisa.id,
            "pergunta": pesquisa.pergunta,
            "opcoes": pesquisa.opcoes.split(','),
            "ativo": pesquisa.ativo
        } for pesquisa in pesquisas
    ]