from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.cliente_model import Cliente
from services.cliente_service import get_cliente, create_cliente
from model.database import get_session

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def read_cliente(session: Session = Depends(get_session)):  # Pasar sesión
    return get_cliente(session)

@router.post("/")
def add_cliente(cliente: Cliente, session: Session = Depends(get_session)):  # Pasar sesión
    return create_cliente(session, cliente)