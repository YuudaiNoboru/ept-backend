from sqlmodel import Field
from .base_model import BaseModel


class Anotacao(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    conteudo: str
    split_id: int | None = Field(default=None, foreign_key="split.id")
    tipo_anotacao_id: int | None = Field(default=None, foreign_key="tipoanotacao.id")