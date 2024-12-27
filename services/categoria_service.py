from repository.categoria_repository import categoria_repository
from schemas.categoria_schema import CategoriaResponse

_categoria_repository = categoria_repository()

def get_categoria():
    categorias = _categoria_repository.get_categoria()
    return [CategoriaResponse.from_orm(categoria) for categoria in categorias]