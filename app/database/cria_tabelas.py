import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Base, engine
import models.aluno
import models.professor
import models.material
import models.aula
import models.grupo_aula
import models.pre_teste
import models.avaliacao
import models.relatorio
import models.material_visualizado
import models.resposta_pre_teste
import models.aula_material


Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")