from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.tienda_model import Tienda
from services.tienda_service import get_tienda, create_tienda
from model.database import get_session

router = APIRouter(prefix="/tiendas", tags=["Tiendas"])

@router.get("/")
def read_tienda(session: Session = Depends(get_session)):  # Pasar sesión
    return get_tienda(session)

@router.post("/")
def add_tienda(tienda: Tienda, session: Session = Depends(get_session)):  # Pasar sesión
    return create_tienda(session, tienda)