from repository.producto_repository import Producto_repository

_producto_repository = Producto_repository()

def get_productos():
    return _producto_repository.get_productos()