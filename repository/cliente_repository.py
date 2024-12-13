from sqlmodel import Session, select
from model.models import Cliente
from model.database import get_session

class Cliente_repository():
    def __init__(self):
        pass
    def get_cliente(self):
        with get_session() as session:
            return session.exec(select(Cliente)).all()

    def create_cliente(session: Session, cliente: Cliente):
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
