from repository.cliente_repository import Cliente_repository
from model.cliente_model import Cliente

_cliente_repository = Cliente_repository()

def get_cliente_by_id(id: int):
    return _cliente_repository.get_cliente_by_id(id)

def create_cliente(cliente: Cliente):
    return _cliente_repository.create_cliente(cliente)