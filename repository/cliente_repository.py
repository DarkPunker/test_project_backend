from sqlmodel import Session, select
from model.cliente_model import Cliente

class Cliente_repository:
    def __init__(self):
        pass

    def get_cliente(self, session: Session):  # Pasar la sesión como argumento
        return session.exec(select(Cliente)).all()

    def create_cliente(self, session: Session, cliente: Cliente):
        session.add(cliente)  # Agregar el cliente a la sesión
        session.commit()  # Confirmar la transacción
        session.refresh(cliente)  # Refrescar el cliente con los valores más recientes
        return cliente  # Retornar el cliente creado