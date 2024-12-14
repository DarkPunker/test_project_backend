from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.cliente_model import Cliente
from services.cliente_service import get_cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def read_cliente():
    return get_cliente()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
