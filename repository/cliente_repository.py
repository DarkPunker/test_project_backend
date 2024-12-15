from sqlmodel import select
from model.cliente_model import Cliente
from model.database import get_session

class Cliente_repository:
    def __init__(self):
        pass

    def get_cliente_by_id(self, id: int):
        with get_session() as session:
            return session.exec(select(Cliente).filter(Cliente.id_usuario == id)).first()

    def create_cliente(self, cliente: Cliente):
        with get_session() as session:
            session.add(cliente)
            session.commit()
            session.refresh(cliente)
            return cliente
        
        
    # def create_cliente(self, session: Session, cliente: Cliente):
    #     session.add(cliente)  # Agregar el cliente a la sesión
    #     session.commit()  # Confirmar la transacción
    #     session.refresh(cliente)  # Refrescar el cliente con los valores más recientes
    #     return cliente  # Retornar el cliente creado