from sqlmodel import SQLModel, Field
from typing_extensions import Annotated
from pydantic import field_validator, EmailStr
import re


# Modelo base com campos comuns
class UsuarioBase(SQLModel):
    nome: Annotated[str, Field(min_length=1, description="Nome do usuário")]
    email: Annotated[EmailStr, Field(unique=True, index=True, description="Email do usuário (deve ser único)")]


# Modelo para criação (entrada da API)
class UsuarioCreate(UsuarioBase):
    senha: Annotated[str, Field(
        min_length=8,
        description="Senha (mínimo 8 caracteres, incluindo maiúscula, número e símbolo)"
    )]
    
    @field_validator('senha')
    def senha_forte(cls, v):
        # Verificar se contém pelo menos uma letra maiúscula
        if not re.search(r'[A-Z]', v):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula")
        
        # Verificar se contém pelo menos um número
        if not re.search(r'[0-9]', v):
            raise ValueError("A senha deve conter pelo menos um número")
        
        # Verificar se contém pelo menos um símbolo
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|]', v):
            raise ValueError("A senha deve conter pelo menos um símbolo")
        
        return v


class Usuario(UsuarioBase, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    senha_hash: str  # Senha com hash armazenada no banco


# Modelo para resposta (saída da API)
class UsuarioResponse(UsuarioBase):
    id: int
    # Sem campo de senha aqui!