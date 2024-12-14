from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.categoria_model import Categoria
from services.categoria_service import get_categoria

router = APIRouter(prefix="/Categoria", tags=["Categoria"])

@router.get("/")
def read_Categoria():
    return get_categoria()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
