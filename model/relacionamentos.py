from sqlmodel import SQLModel, Field

# Link model para a relação muitos-para-muitos entre Atividade e Assunto
class AtividadeAssunto(SQLModel, table=True):
    atividade_id: int = Field(foreign_key="atividade.id", primary_key=True)
    assunto_id: int = Field(foreign_key="assunto.id", primary_key=True)


# Tabela de relacionamento para Split e Assunto (many-to-many)
class SplitAssunto(SQLModel, table=True):
    split_id: int = Field(foreign_key="split.id", primary_key=True)
    assunto_id: int = Field(foreign_key="assunto.id", primary_key=True)