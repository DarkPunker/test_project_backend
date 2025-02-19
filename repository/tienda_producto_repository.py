from sqlmodel import Session, select
from model.tienda_producto_model import TiendaProducto
from model.database import get_session

class TiendaProductoRepository:
    def __init__(self):
        pass

    def get_tienda_producto(self):
        with get_session() as session:
            return session.exec(select(TiendaProducto)).all()

    def create_tienda_producto(self, tienda_producto: TiendaProducto):
        with get_session() as session:
            session.add(tienda_producto)
            session.commit()
            session.refresh(tienda_producto)
            return tienda_producto
        
    def edit_tienda_producto(self, tienda_producto: TiendaProducto):
        with get_session() as session:
            session.merge(tienda_producto)  
            session.commit()      
            session.refresh(tienda_producto)  
            return tienda_producto
