from sqlmodel import select
from model.database import get_session
from model.orden_compra_model import OrdenCompra

class Orden_Compra_repository:
    def __init__(self):
        pass

    def get_orden_compra_by_cliente(self, cc_cliente: int):
        with get_session() as session:
            return session.exec(select(OrdenCompra).filter(OrdenCompra.cc_cliente == cc_cliente)).all()
    
    def get_orden_compra_by_tienda_producto(self, id_tienda_producto: int):
        with get_session() as session:
            return session.exec(select(OrdenCompra).filter(OrdenCompra.id_tienda_producto == id_tienda_producto)).all()
        
    def create_orden_compra(self, orden: OrdenCompra):
        with get_session() as session:
            session.add(orden)
            session.commit()
            session.refresh(orden)
            return orden
        
    def edit_orden_compra(self, orden: OrdenCompra):
        with get_session() as session:
            session.merge(orden)  
            session.commit()      
            session.refresh(orden)  
            return orden