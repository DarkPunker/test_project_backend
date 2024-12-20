from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.producto_model import Producto
from services.producto_service import get_productos

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def read_productos():
    return get_productos()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
