from repository.librerias_repository import librerias_repository

_librerias_repository = librerias_repository()

def get_librerias():
    return _librerias_repository.get_librerias()