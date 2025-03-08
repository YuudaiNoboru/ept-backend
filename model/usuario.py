from sqlmodel import SQLModel, Field
from typing_extensions import Annotated



# Modelo base com campos comuns
class UsuarioBase(SQLModel):
    nome: str
    email: Annotated[str, Field(unique=True, index=True)]

# Modelo para criação (entrada da API)
class UsuarioCreate(UsuarioBase):
    senha: str  # Senha em texto plano para criação

class Usuario(UsuarioBase, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    senha_hash: str  # Senha com hash armazenada no banco

# Modelo para resposta (saída da API)
class UsuarioResponse(UsuarioBase):
    id: int
    # Sem campo de senha aqui!