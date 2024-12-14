from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.tienda_producto_model import TiendaProducto
from services.tienda_producto_service import get_tienda_producto
from repository.tienda_producto_repository import TiendaProductoRepository
from model.database import get_session

router = APIRouter(prefix="/tienda_producto", tags=["TiendaProducto"])

@router.get("/")
def read_tienda_producto():
    return get_tienda_producto()

#@router.post("/")
#def create_tienda_producto(
#    tienda_producto: TiendaProducto, session: Session = Depends(get_session)
#):
#    repository = TiendaProductoRepository()
#    return repository.create_tienda_producto(session, tienda_producto)
