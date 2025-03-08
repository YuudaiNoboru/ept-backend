from sqlmodel import SQLModel, Field
from datetime import datetime
from .base_model import BaseModel


class Split(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tempo_gasto: int  # Tempo em minutos
    atividade_id: int | None = Field(default=None, foreign_key="atividade.id")

# Tabela de relacionamento para Split e Assunto (many-to-many)
class SplitAssunto(SQLModel, table=True):
    split_id: int = Field(foreign_key="split.id", primary_key=True)
    assunto_id: int = Field(foreign_key="assunto.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)