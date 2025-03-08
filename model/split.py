from sqlmodel import SQLModel, Field, Relationship
from typing import List
from typing_extensions import Annotated
from .atividade import Atividade
from .usuario import Usuario


class Split(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tempo_gasto: int  # Tempo em minutos
    atividade_id: int | None = Field(default=None, foreign_key="atividade.id")
    atividade: Atividade | None = Relationship(back_populates="splits")
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    usuario: Usuario | None = Relationship(back_populates="splits")
    anotacoes: List["Anotacao"] = Relationship(back_populates="split")
    assuntos: List["Assunto"] = Relationship(
        back_populates="splits", link_model=SplitAssunto
    )
