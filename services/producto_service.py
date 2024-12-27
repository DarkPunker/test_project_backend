from repository.producto_repository import Producto_repository
from schemas.tienda_schema import ProductoResponse

_producto_repository = Producto_repository()

def get_productos():
    prductos = _producto_repository.get_productos()
    return [ProductoResponse.from_orm(producto) for producto in prductos]