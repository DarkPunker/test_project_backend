from typing import List
from fastapi import APIRouter
from model.orden_compra_model import OrdenCompra
from schemas.error_response import error_responses
from services.orden_compra_service import create_orden_compra, edit_orden_compra, get_orden_compra_by_cliente, get_orden_compra_by_tienda_producto


router = APIRouter(prefix="/orden_compra", tags=["OrdenCompra"])

@router.get("/get_orden_compra_by_cliente/{cc_cliente}", responses=error_responses, response_model=List[OrdenCompra], summary='Read orden_compra cc')
def get_orden_compra_by_cliente_router(cc_cliente: int):
    return get_orden_compra_by_cliente(cc_cliente)

@router.get("/get_orden_compra_by_tienda_producto/{id_tienda_producto}", responses=error_responses, response_model=List[OrdenCompra], summary='Read orden_compra idtp')
def get_orden_compra_by_tienda_producto_router(id_tienda_producto: int):
    return get_orden_compra_by_tienda_producto(id_tienda_producto)

@router.post("/add_orden_compr", responses=error_responses, response_model=OrdenCompra, summary='Add orden compra')
def create_orden_compra_router(orden_compra: OrdenCompra):
    return create_orden_compra(orden_compra)

@router.post("/edit_orden_compra", responses=error_responses, response_model=OrdenCompra, summary='Edit orden compra')
def edit_orden_compra_router(orden_compra: OrdenCompra):
    return edit_orden_compra(orden_compra)
