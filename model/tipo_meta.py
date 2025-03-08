from sqlmodel import SQLModel, Field, Relationship
from typing import List
from typing_extensions import Annotated
from .usuario import Usuario


class TipoMeta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    usuario: Usuario | None = Relationship(back_populates="tipos_meta")
    atividades: List["Atividade"] = Relationship(back_populates="tipo_meta")
