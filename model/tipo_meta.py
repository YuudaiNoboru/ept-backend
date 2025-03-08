from sqlmodel import Field
from .base_model import BaseModel


class TipoMeta(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None