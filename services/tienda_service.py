from repository.tienda_repository import Tienda_repository
from model.tienda_model import Tienda
from sqlmodel import Session  # Importa Session

_tienda_repository = Tienda_repository()

def get_tienda(session: Session):
    return _tienda_repository.get_tienda(session)

def create_tienda(session: Session, tienda: Tienda):
    return _tienda_repository.create_tienda(session, tienda)