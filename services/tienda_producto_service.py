from repository.tienda_producto_repository import TiendaProductoRepository

_tienda_producto_repository = TiendaProductoRepository()

def get_tienda_producto():
    return _tienda_producto_repository.get_tienda_producto()
