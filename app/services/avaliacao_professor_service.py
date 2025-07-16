from app.repositories import avaliacao_professor_repo
from app.models.avaliacao_professor import AvaliacaoProfessor

def criar_avaliacao(avaliacao_data):
    return avaliacao_professor_repo.criar_avaliacao(avaliacao_data)

def registrar_avaliacao(data):
    campos_obrigatorios = ["professor_id", "aluno_id", "grupo", "participacao", "dominio_tema"]
    for campo in campos_obrigatorios:
        if campo not in data:
            return {"error": f"Campo obrigatório ausente: {campo}"}
    if "nota_pre_teste" not in data:
        data["nota_pre_teste"] = None
    return avaliacao_professor_repo.salvar_avaliacao(data)

def obter_por_grupo(grupo):
    avaliacoes = avaliacao_professor_repo.listar_por_grupo(grupo)

    # Média de participação e domínio do tema
    if not avaliacoes:
        return {"grupo": grupo, "avaliacoes": [], "media_participacao": 0, "media_dominio": 0}

    soma_participacao = sum([a.participacao for a in avaliacoes])
    soma_dominio = sum([a.dominio_tema for a in avaliacoes])
    total = len(avaliacoes)

    return {
        "grupo": grupo,
        "avaliacoes": [
            {
                "aluno_id": a.aluno_id,
                "participacao": a.participacao,
                "dominio_tema": a.dominio_tema,
                "nota_pre_teste": a.nota_pre_teste
            }
            for a in avaliacoes
        ],
        "media_participacao": round(soma_participacao / total, 2),
        "media_dominio": round(soma_dominio / total, 2)
    }
def listar_avaliacoes():
    return avaliacao_professor_repo.listar_avaliacoes()

def aluno_ja_respondeu(avaliacao_id, aluno_id):
    return avaliacao_professor_repo.aluno_ja_respondeu(avaliacao_id, aluno_id)
