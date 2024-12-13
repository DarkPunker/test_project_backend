from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..model.database import get_session
from ..model.models import Producto
from ..repository.producto_crud import get_productos, create_producto

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def read_productos(session: Session = Depends(get_session)):
    return get_productos(session)

@router.post("/")
def add_producto(producto: Producto, session: Session = Depends(get_session)):
    return create_producto(session, producto)
