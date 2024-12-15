from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.usuario_model import Usuario
from services.usuario_service import get_usuario, create_usuario
from model.database import get_session

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.get("/")
def read_usuario(session: Session = Depends(get_session)):  # Pasar sesión
    return get_usuario(session)

@router.post("/")
def add_usuario(usuario: Usuario, session: Session = Depends(get_session)):  # Pasar sesión
    return create_usuario(session, usuario)