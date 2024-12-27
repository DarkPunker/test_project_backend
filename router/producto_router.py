from typing import List
from fastapi import APIRouter
from schemas.error_response import error_responses
from schemas.tienda_schema import ProductoResponse
from services.producto_service import get_productos

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/get_all_produts",responses=error_responses, response_model=List[ProductoResponse], summary='Read all products')
def read_productos():
    return get_productos()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
