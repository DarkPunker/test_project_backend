from sqlmodel import Session, select
from model.tienda_model import Tienda

class Tienda_repository:
    def __init__(self):
        pass

    def get_tienda(self, session: Session):
        return session.exec(select(Tienda)).all()

    def create_tienda(self, session: Session, tienda: Tienda):
        session.add(tienda)  # Agregar la tienda a la sesión
        session.commit()     # Confirmar la transacción
        session.refresh(tienda)  # Refrescar los datos de la tienda (si es necesario)
        return tienda  # Retornar el objeto tienda persistido