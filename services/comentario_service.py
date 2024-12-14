from repository.comentario_repository import comentario_repository

_comentario_repository = comentario_repository()

def get_comentario():
    return _comentario_repository.get_comentario()