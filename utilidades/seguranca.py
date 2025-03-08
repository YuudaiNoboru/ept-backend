from jose import JWTError, jwt
from passlib.context import CryptContext
from model.usuario import Usuario
from sqlmodel import Session, select
from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utilidades.database import get_session
from model.token import TokenData


# Configurações para JWT
SECRET_KEY = "sua_chave_secreta_aqui"
ALGORITHM = "HS256"


# Configurações para criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Função para verificar a senha
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# Função para gerar o hash da senha
def get_password_hash(password: str):
    return pwd_context.hash(password)


# Função para autenticar o usuário
def authenticate_user(email: str, password: str, db: Session):
    user = db.exec(select(Usuario).where(Usuario.email == email)).first()
    if not user:
        return False
    if not verify_password(password, user.senha_hash):
        return False
    return user


# Função para criar o token de acesso
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Função para obter o usuário atual
async def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")),
    db: Session = Depends(get_session),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = db.exec(select(Usuario).where(Usuario.email == token_data.email)).first()
    if user is None:
        raise credentials_exception
    return user
