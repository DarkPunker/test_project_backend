from typing import List
from fastapi import APIRouter
from model.tienda_producto_model import TiendaProducto
from schemas.error_response import error_responses
from schemas.tienda_schema import TiendaProductoRequest, TiendaProductoResponse
from services.tienda_producto_service import edit_tienda_producto, get_tienda_producto
from repository.tienda_producto_repository import TiendaProductoRepository

router = APIRouter(prefix="/tienda_producto", tags=["TiendaProducto"])

@router.get("/get_all_store_product", responses=error_responses, response_model=List[TiendaProductoResponse], summary='Read Tienda Producto')
def read_tienda_producto():
    return get_tienda_producto()

@router.post("/add_store", responses=error_responses, response_model=TiendaProductoResponse, summary='Add Store Product')
def create_tienda_producto(tienda_producto: TiendaProductoRequest):
    return create_tienda_producto(tienda_producto)

@router.post("/edit_store_product", responses=error_responses, response_model=TiendaProducto, summary='Edit Store Product')
def edit_tienda_producto_router(tienda_producto: TiendaProducto):
    return edit_tienda_producto(tienda_producto)
