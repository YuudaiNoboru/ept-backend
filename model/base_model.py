from sqlmodel import SQLModel, Field
from typing_extensions import Annotated
from datetime import datetime


class BaseModel(SQLModel):
    """Classe base para todos os modelos com campos comuns"""
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
    
    class Config:
        arbitrary_types_allowed = True