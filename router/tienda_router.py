from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.tienda_model import Tienda
from services.tineda_service import get_tienda

router = APIRouter(prefix="/tiendas", tags=["Tienda"])

@router.get("/")
def read_tienda():
    return get_tienda()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
