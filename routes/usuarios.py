from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session
from utilidades.database import get_session
from model.usuario import Usuario, UsuarioResponse, UsuarioCreate
from utilidades.seguranca import get_password_hash, get_current_user


# Router
router = APIRouter()


# Rota para criar um novo usuário
@router.post("/usuarios/", response_model=UsuarioResponse)
async def create_user(usuario: UsuarioCreate, db: Session = Depends(get_session)):
    # Criar novo objeto Usuario para o banco de dados
    usuario_db = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=get_password_hash(usuario.senha)
    )
    
    try:
        db.add(usuario_db)
        db.commit()
        db.refresh(usuario_db)
        return usuario_db  # SQLModel automaticamente converte para UsuarioResponse
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Um usuário com este email já existe."
        )


# Rota para obter o usuário atual
@router.get("/usuarios/me/", response_model=Usuario)
async def read_users_me(current_user: Usuario = Depends(get_current_user)):
    return current_user