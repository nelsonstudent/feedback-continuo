from datetime import datetime

from streamlit import form
from app.repositories.material_repo import salvar_arquivo, add_material, material_inacessado

def upload_material_service(titulo, arquivo, link, disponivel_ate):
    título = form.get('título')
    disponivel = form.get('disponivel_ate')
    disponivel_ate = datetime.fromisoformat(disponivel) if disponivel else None
    # Verifica se o arquivo foi enviado
    arquivo_path = None
    if arquivo:
        filename = f"{int(datetime.utcnow().timestamp())}_{arquivo.filename}"
        arquivo_path, atualizado_em = salvar_arquivo(arquivo, titulo)
    
    link = form.get('link') or None
    return add_material(titulo, arquivo_path, link, disponivel_ate)
    novo_material = add_material(titulo, arquivo_path, link, disponivel_ate)

    return novo_material

def obter_materiais_inacessados():
    return material_inacessado()
