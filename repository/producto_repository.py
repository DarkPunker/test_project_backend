from sqlmodel import Session, select
from model.models import Producto
from model.database import get_session

class Producto_repository():
    def __init__(self):
        pass
    def get_productos(self):
        with get_session() as session:
            return session.exec(select(Producto)).all()

    def create_producto(session: Session, producto: Producto):
        session.add(producto)
        session.commit()
        session.refresh(producto)
        return producto
