from typing import List
from model.tienda_producto_model import TiendaProducto
from repository.tienda_producto_repository import TiendaProductoRepository
from schemas.tienda_schema import TiendaProductoRequest, TiendaProductoResponse

_tienda_producto_repository = TiendaProductoRepository()

def get_tienda_producto() -> List[TiendaProductoResponse]:
    tiendas = _tienda_producto_repository.get_tienda_producto()
    return [TiendaProductoResponse.from_orm(tienda) for tienda in tiendas]

def create_tienda_producto(store_product: TiendaProductoRequest):
    tienda_producto = TiendaProducto(
        precio= store_product.precio,
        calificacion= store_product.calificacion,
        stock= store_product.stock,
        caracteristicas= store_product.caracteristicas,
        descripcion= store_product.descripcion,
        id_tienda= store_product.id_tienda,
        id_producto= store_product.id_producto,
    )
    tienda_product = _tienda_producto_repository.create_tienda_producto(tienda_producto)
    return TiendaProductoResponse.from_orm(tienda_product)

def edit_tienda_producto(tiendaproducto: TiendaProducto):
    return _tienda_producto_repository.edit_tienda_producto(tiendaproducto)
     
