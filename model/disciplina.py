from sqlmodel import SQLModel, Field, Relationship
from typing_extensions import Annotated
from model.usuario import Usuario


class Disciplina(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    usuario: Usuario | None = Relationship(back_populates="disciplinas")
