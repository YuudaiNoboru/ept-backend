from model.token import Token
from utilidades.seguranca import authenticate_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from utilidades.seguranca import create_access_token
from datetime import timedelta
from utilidades.database import Session, get_session


# Router
router = APIRouter(tags=["autenticação"])


# Configurações para JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Rota para login e obtenção do token
@router.post("/token", response_model=Token, summary="Obter token de acesso")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)
):
    """
    Obtém um token de acesso JWT para autenticação.
    
    - **username**: Email do usuário (usa o campo 'username' do form padrão OAuth2)
    - **password**: Senha do usuário
    
    Retorna um token de acesso que deve ser usado no cabeçalho Authorization como "Bearer {token}"
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}