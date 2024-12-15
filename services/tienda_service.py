from fastapi import HTTPException
from repository.tienda_repository import Tienda_repository
from repository.usuario_repository import Usuario_repository
from model.tienda_model import Tienda
from schemas.tienda_schema import TiendaReponse, TiendaRequest

_tienda_repository = Tienda_repository()
_usuario_repository = Usuario_repository()

def get_tienda():
    tiendas = _tienda_repository.get_tienda()

    tienda_responses = [TiendaReponse.from_orm(tienda) for tienda in tiendas]

    return tienda_responses

def create_tienda(tienda: TiendaRequest):
    user = _usuario_repository.get_usuario_by_email(tienda.email)
    tiendaModel = Tienda(
        nombre = tienda.nombre,
        redes = tienda.redes,
        celular = tienda.celular,
        direccion = tienda.direccion,
        lat = tienda.lat,
        long = tienda.long,
        id_usuario = user.id
    )
    return _tienda_repository.create_tienda(tiendaModel)