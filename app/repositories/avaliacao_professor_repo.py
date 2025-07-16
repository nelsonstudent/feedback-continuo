import datetime
from app import db
from app.models.avaliacao_professor import AvaliacaoProfessor

def criar_avaliacao(avaliacao_data):
    avaliacao = AvaliacaoProfessor(**avaliacao_data)
    avaliacao.data_avaliacao = datetime.utcnow()  # Garantir que a data seja atualizada
    avaliacao.professor_id = avaliacao_data['professor_id']
    avaliacao.aluno_id = avaliacao_data['aluno_id']
    avaliacao.grupo = avaliacao_data['grupo']
    avaliacao.participacao = avaliacao_data['participacao']
    avaliacao.dominio_tema = avaliacao_data['dominio_tema'] # integração futura
    avaliacao.nota_pre_teste = avaliacao_data.get('nota_pre_teste', None)  # integração futura

    db.session.add(avaliacao)
    db.session.commit()
    return avaliacao

def salvar_avaliacao(avaliacao_data):
    nova_avaliacao = AvaliacaoProfessor(**avaliacao_data)
    db.session.add(nova_avaliacao)
    db.session.commit()
    return nova_avaliacao

def listar_avaliacoes():
    return AvaliacaoProfessor.query.all()

def listar_todas():
    return AvaliacaoProfessor.query.all()

def aluno_ja_respondeu(avaliacao_id, aluno_id):
    return AvaliacaoProfessor.query.filter_by(avaliacao_id=avaliacao_id, aluno_id=aluno_id).first() is not None
