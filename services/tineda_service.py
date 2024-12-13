from repository.tienda_repository import Tienda_repository

_tienda_repository = Tienda_repository()

def get_tienda():
    return _tienda_repository.get_tienda()