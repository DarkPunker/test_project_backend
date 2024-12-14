from sqlmodel import Session, select
from model.tienda_model import Tienda
from model.database import get_session

class Tienda_repository():
    def __init__(self):
        pass
    def get_tienda(self):
        with get_session() as session:
            return session.exec(select(Tienda)).all()

    def create_tienda(session: Session, tienda: Tienda):
        session.add(tienda)
        session.commit()
        session.refresh(tienda)
        return tienda
