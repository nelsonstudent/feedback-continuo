from app.database.sias_db import Base, engine
import app.models.aluno
import app.models.professor
import app.models.material
import app.models.aula
import app.models.grupo_aula
import app.models.pre_teste
import app.models.avaliacao
import app.models.relatorio
import app.models.material_visualizado
import app.models.resposta_pre_teste
import app.models.aula_material


Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")