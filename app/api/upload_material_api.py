from flask import Blueprint, request, jsonify, abort
from app.services.upload_material_service import upload_material, get_materiais_inacessados

upload_material_bp = Blueprint('upload_material', __name__, url_prefix='/upload_material')

@upload_material_bp.route('/upload', methods=['POST'])
def upload():
    arquivo_object = request.files.get('arquivo')
    if not arquivo_object:
        abort(400, 'Arquivo é obrigatório.')
    if arquivo_object.filename == '':
        abort(400, 'Nome do arquivo não pode ser vazio.')
    if arquivo_object.content_type not in ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        abort(400, 'Tipo de arquivo não suportado. Apenas PDF e DOCX são permitidos.')
    novo_material = upload_material(request.form['titulo'], arquivo_object, request.form.get('link'), request.form.get('disponivel_ate'))
    data = request.json
    titulo = data.get('titulo')
    arquivo = arquivo_object
    link = data.get('link')
    disponivel_ate = data.get('disponivel_ate')

    if not titulo or not arquivo:
        abort(400, 'Título e arquivo são obrigatórios.')

    novo_material = upload_material(titulo, arquivo, link, disponivel_ate)
    return jsonify(novo_material), 201

@upload_material_bp.route('/materiais/inacessados', methods=['GET'])
def materiais_inacessados():
    materiais = get_materiais_inacessados()
    return jsonify([
        {'id': m.id, 'titulo': m.titulo, 'criado_em': m.criado_em.isoformat()}
        for m in materiais
    ]), 200
