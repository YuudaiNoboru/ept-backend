from pydantic import BaseModel
from typing import Optional


# Modelo para o token
class Token(BaseModel):
    access_token: str
    token_type: str


# Modelo para o token data
class TokenData(BaseModel):
    email: Optional[str] = None