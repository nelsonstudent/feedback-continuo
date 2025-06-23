from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

aula_material = Table(
    "aula_material", Base.metadata,
    Column("aula_id", Integer, ForeignKey("aulas.id"), primary_key=True),
    Column("material_id", Integer, ForeignKey("materiais.id"), primary_key=True)
)