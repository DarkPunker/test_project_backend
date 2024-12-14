from repository.categoria_repository import categoria_repository

_categoria_repository = categoria_repository()

def get_categoria():
    return _categoria_repository.get_categoria()