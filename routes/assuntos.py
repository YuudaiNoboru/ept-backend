from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from model.assunto import Assunto
from model.disciplina import Disciplina
from utilidades.database import get_session

router = APIRouter(prefix="/assuntos", tags=["assuntos"])


@router.post("/", response_model=Assunto)
def criar_assunto(assunto: Assunto, session: Session = Depends(get_session)):
    # Verificar se a disciplina existe
    if assunto.disciplina_id:
        disciplina = session.get(Disciplina, assunto.disciplina_id)
        if not disciplina:
            raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    
    # Se for um subassunto, verificar se o pai existe
    if assunto.pai_id:
        pai = session.get(Assunto, assunto.pai_id)
        if not pai:
            raise HTTPException(status_code=404, detail="Assunto pai não encontrado")
        # O nível do filho é o nível do pai + 1
        assunto.nivel = pai.nivel + 1
    
    session.add(assunto)
    session.commit()
    session.refresh(assunto)
    return assunto


@router.get("/{assunto_id}", response_model=Assunto)
def obter_assunto(assunto_id: int, session: Session = Depends(get_session)):
    assunto = session.get(Assunto, assunto_id)
    if not assunto:
        raise HTTPException(status_code=404, detail="Assunto não encontrado")
    return assunto


@router.get("/", response_model=List[Assunto])
def listar_assuntos(disciplina_id: int = None, session: Session = Depends(get_session)):
    query = select(Assunto)
    if disciplina_id:
        query = query.where(Assunto.disciplina_id == disciplina_id)
    assuntos = session.exec(query).all()
    return assuntos


@router.put("/{assunto_id}", response_model=Assunto)
def atualizar_assunto(assunto_id: int, assunto_atualizado: Assunto, session: Session = Depends(get_session)):
    assunto = session.get(Assunto, assunto_id)
    if not assunto:
        raise HTTPException(status_code=404, detail="Assunto não encontrado")
    
    # Verificar se a disciplina existe (se for alterada)
    if assunto_atualizado.disciplina_id:
        disciplina = session.get(Disciplina, assunto_atualizado.disciplina_id)
        if not disciplina:
            raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    
    # Se for um subassunto, verificar se o pai existe
    if assunto_atualizado.pai_id:
        pai = session.get(Assunto, assunto_atualizado.pai_id)
        if not pai:
            raise HTTPException(status_code=404, detail="Assunto pai não encontrado")
        # O nível do filho é o nível do pai + 1
        assunto_atualizado.nivel = pai.nivel + 1
    
    assunto.sqlmodel_update(assunto_atualizado)
    session.add(assunto)
    session.commit()
    session.refresh(assunto)
    return assunto


@router.delete("/{assunto_id}")
def deletar_assunto(assunto_id: int, session: Session = Depends(get_session)):
    assunto = session.get(Assunto, assunto_id)
    if not assunto:
        raise HTTPException(status_code=404, detail="Assunto não encontrado")
    
    # Verificar se o assunto tem filhos
    filhos = session.exec(select(Assunto).where(Assunto.pai_id == assunto_id)).all()
    if filhos:
        raise HTTPException(status_code=400, detail="Não é possível deletar um assunto que possui subassuntos")
    
    session.delete(assunto)
    session.commit()
    return {"message": "Assunto deletado com sucesso"}