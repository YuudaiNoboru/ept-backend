from sqlmodel import SQLModel, Field, Relationship
from typing import List
from typing_extensions import Annotated
from .concurso import Concurso
from .disciplina import Disciplina
from .assunto import Assunto
from .tipo_meta import TipoMeta
from .usuario import Usuario


class Atividade(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str | None = None
    quantidade_meta: int  # Quantidade total da meta (ex: 20 questões)
    quantidade_concluida_total: int = Field(
        default=0
    )  # Soma das quantidades concluídas
    quantidade_sucesso_total: int = Field(default=0)  # Soma das quantidades de sucesso
    tempo_total: int = Field(
        default=0
    )  # Soma do tempo gasto em todos os splits (em minutos)
    concurso_id: int | None = Field(default=None, foreign_key="concurso.id")
    concurso: Concurso | None = Relationship(back_populates="atividades")
    disciplina_id: int | None = Field(default=None, foreign_key="disciplina.id")
    disciplina: Disciplina | None = Relationship(back_populates="atividades")
    assuntos: List["Assunto"] = Relationship(
        back_populates="atividades", link_model=AtividadeAssunto
    )
    tipo_meta_id: int | None = Field(default=None, foreign_key="tipometa.id")
    tipo_meta: TipoMeta | None = Relationship(back_populates="atividades")
    usuario_id: Annotated[int, Field(foreign_key="usuario.id")]
    usuario: Usuario | None = Relationship(back_populates="atividades")
    splits: List["Split"] = Relationship(back_populates="atividade")
