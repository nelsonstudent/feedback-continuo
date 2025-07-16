import os
from datetime import datetime
from app import db
from app.models.upload_material import UploadMaterial   

STORAGE = os.getenv('UPLOAD_STORAGE', 'upload_material')

def salvar_arquivo(storage_obj, nome_arquivo):
    os.makedirs(STORAGE, exist_ok=True)
    path = os.path.join(STORAGE, nome_arquivo)
    storage_obj.save(path)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    return path, atualizado_em

def add_material(titulo, arquivo_path=None, Link=None, disponivel_ate=None):
    novo_material = UploadMaterial(
        nome_arquivo=titulo,
        arquivo=arquivo_path,
        link=Link,
        disponivel_ate=disponivel_ate
    )
    db.session.add(novo_material)
    db.session.commit()
    return novo_material

def material_inacessado():
    now = datetime.utcnow()
    return UploadMaterial.query.filter(
        UploadMaterial.ultimo_acesso.is_(None),
        UploadMaterial.disponivel_ate.is_(None) | (UploadMaterial.disponivel_ate >= now)
    ).all()