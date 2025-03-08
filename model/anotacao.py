from sqlmodel import SQLModel, Field, Relationship
from typing_extensions import Annotated
from .split import Split
from .tipo_anotacao import TipoAnotacao
from .usuario import Usuario


class Anotacao(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    conteudo: str
    split_id: int | None = Field(default=None, foreign_key="split.id")
    split: Split | None = Relationship(back_populates="anotacoes")
    tipo_anotacao_id: int | None = Field(default=None, foreign_key="tipoanotacao.id")
    tipo_anotacao: TipoAnotacao | None = Relationship(back_populates="anotacoes")
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    usuario: Usuario | None = Relationship(back_populates="anotacoes")
