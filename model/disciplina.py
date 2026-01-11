from typing import List, Optional
from sqlmodel import Field, Relationship
from .base_model import BaseModel


class Disciplina(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    
    # Relacionamento com assuntos
    assuntos: List["Assunto"] = Relationship(back_populates="disciplina")