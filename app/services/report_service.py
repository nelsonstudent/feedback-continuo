from app.repositorys.report_repo import (
    coletar_dados,
    gerar_relatorio as gerar_relatorio_excel,
    gerar_pdf,
    salvar_arquivo,
    registrar_relatorio
)
from app.repositorys.authorization_repo import verificar_liberacao

def gerar_relatorio(aula_id):
    if not verificar_liberacao(aula_id):
        return {"error": "Acesso não autorizado"}

    dados = coletar_dados(aula_id)
    relatorio_excel = gerar_relatorio_excel(dados)
    relatorio_pdf = gerar_pdf(dados)

    caminho_excel = salvar_arquivo(aula_id, relatorio_excel)
    caminho_pdf = salvar_arquivo(aula_id, relatorio_pdf)

    registrar_relatorio(aula_id, caminho_excel)
    registrar_relatorio(aula_id, caminho_pdf)

    return {"message": "Relatórios gerados com sucesso", "caminhos": [caminho_excel, caminho_pdf]}