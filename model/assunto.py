from typing import List, Optional
from sqlmodel import Field, Relationship
from .base_model import BaseModel


class Assunto(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    nivel: int = Field(default=0)  # Nível hierárquico (0 para raiz, 1 para filho, etc.)
    pai_id: int | None = Field(default=None, foreign_key="assunto.id")  # Referência para o assunto pai
    disciplina_id: int | None = Field(default=None, foreign_key="disciplina.id")
    
    # Relacionamentos
    disciplina: Optional["Disciplina"] = Relationship(back_populates="assuntos")
    pai: Optional["Assunto"] = Relationship(
        back_populates="filhos",
        sa_relationship_kwargs={
            "remote_side": "Assunto.id",
        }
    )
    filhos: List["Assunto"] = Relationship(back_populates="pai")
