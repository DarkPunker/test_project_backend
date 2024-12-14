from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.librerias_model import Librerias
from services.librerias_service import get_librerias

router = APIRouter(prefix="/librerias", tags=["librerias"])

@router.get("/")
def read_librerias():
    return get_librerias()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
