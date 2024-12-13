from sqlmodel import Session, select
from ..model.models import Producto

def get_productos(session: Session):
    return session.exec(select(Producto)).all()

def create_producto(session: Session, producto: Producto):
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto
