from repository.cliente_repository import Cliente_repository
from model.cliente_model import Cliente
from sqlmodel import Session  # Importa Session

_cliente_repository = Cliente_repository()

def get_cliente(session: Session):
    return _cliente_repository.get_cliente(session)

def create_cliente(session: Session, cliente: Cliente):
    return _cliente_repository.create_cliente(session, cliente)