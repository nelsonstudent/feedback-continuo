from app import db
from app.models.survey import Survey, Resposta
from datetime import datetime
from sqlalchemy.exc import IntegrityError

def criar_pesquisa(pergunta, opcoes):
    nova_pesquisa = Survey(pergunta=pergunta, opcoes=','.join(opcoes))
    db.session.add(nova_pesquisa)
    db.session.commit()
    try:
        db.session.commit()
        return nova_pesquisa
    except IntegrityError:
        db.session.rollback()
        return None
def listar_pesquisas_ativas():
    return Survey.query.filter_by(ativo=True).all()
def buscar_pesquisa_por_id(survey_id):
    return Survey.query.get(id=survey_id)
def atualizar_pesquisa(survey_id, pergunta=None, descricao=None, opcoes=None, ativo=None):
    pesquisa = Survey.query.get(survey_id)
    if not pesquisa:
        return None
    
    if pergunta:
        pesquisa.pergunta = pergunta
    if descricao:
        pesquisa.descricao = descricao
    if opcoes:
        pesquisa.opcoes = ','.join(opcoes)
    if ativo is not None:
        pesquisa.ativo = ativo
    
    db.session.commit()
    return pesquisa
def salvar_resposta(survey_id, aluno_id, resposta):
    nova_resposta = Resposta(survey_id=survey_id, aluno_id=aluno_id, resposta=resposta)
    db.session.add(nova_resposta)
    try:
        db.session.commit()
        return nova_resposta
    except IntegrityError:
        db.session.rollback()
        return None
def aluno_ja_respondeu(survey_id, aluno_id):
    return Resposta.query.filter_by(survey_id=survey_id, aluno_id=aluno_id).first() is not None
