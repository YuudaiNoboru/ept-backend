from sqlmodel import Field
from .base_model import BaseModel


class Assunto(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    disciplina_id: int | None = Field(default=None, foreign_key="disciplina.id")
