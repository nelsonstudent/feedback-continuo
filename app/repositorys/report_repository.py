import os, time
from app import db
from app.models.report import Report
from io import BytesIO
import pandas as pd

STORAGE_PATH = os.getnv('REPORT_STORAGE_PATH', 'reports')

def coletar_dados(aula_id):
    """
    Coleta dados de relatórios de uma aula específica.
    """
    return{'aula_id': aula_id, 'dados': []}

def gerar_relatorio(aula_id):
    """
    Gera um relatório para uma aula específica.
    """
    dados = coletar_dados(aula_id)
    df = pd.DataFrame(dados['dados'])
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer

def gerar_pdf(dados):
    df = pd.DataFrame(dados['dados'])
    buf = BytesIO()
    df.to_csv(buf, index=False)
    buf.seek(0)
    return buf

def salvar_arquivo(aula_id, buffer):
    """
    Salva o arquivo gerado no sistema de arquivos.
    """
    os.makedirs(STORAGE_PATH, exist_ok=True)
    fn = f"{aula_id}_{int(time.time())}.csv"
    path = os.path.join(STORAGE_PATH, fn)
    with open(path,'wb') as f: f.write(buffer.read())
    return path

def registrar_relatorio(aula_id, url):
    """
    Registra o relatório no banco de dados.
    """
    relatorio = Report(aula_id=aula_id, url=url)
    db.session.add(relatorio)
    db.session.commit()
    return relatorio
