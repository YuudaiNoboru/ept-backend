from sqlmodel import SQLModel, Field, Relationship
from typing_extensions import Annotated
from .disciplina import Disciplina
from .usuario import Usuario


class Assunto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    disciplina_id: int | None = Field(default=None, foreign_key="disciplina.id")
    disciplina: Disciplina | None = Relationship(back_populates="assuntos")
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    usuario: Usuario | None = Relationship(back_populates="assuntos")
