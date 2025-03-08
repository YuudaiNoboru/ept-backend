from sqlmodel import SQLModel, Field
from datetime import datetime
from .base_model import BaseModel


class Atividade(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    quantidade_meta: int  # Quantidade total da meta (ex: 20 questões)
    quantidade_concluida_total: int = Field(default=0)  # Soma das quantidades concluídas
    quantidade_sucesso_total: int = Field(default=0)  # Soma das quantidades de sucesso
    tempo_total: int = Field(default=0)  # Soma do tempo gasto em todos os splits (em minutos)
    concurso_id: int | None = Field(default=None, foreign_key="concurso.id")
    disciplina_id: int | None = Field(default=None, foreign_key="disciplina.id")
    tipo_meta_id: int | None = Field(default=None, foreign_key="tipometa.id")

# Tabela de relacionamento para Atividade e Assunto (many-to-many)
class AtividadeAssunto(SQLModel, table=True):
    atividade_id: int = Field(foreign_key="atividade.id", primary_key=True)
    assunto_id: int = Field(foreign_key="assunto.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
