from repository.cliente_repository import Cliente_repository

_cliente_repository = Cliente_repository()

def get_cliente():
    return _cliente_repository.get_cliente()