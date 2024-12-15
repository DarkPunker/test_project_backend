from sqlmodel import select
from model.tienda_model import Tienda
from model.database import get_session

class Tienda_repository:
    def __init__(self):
        pass

    def get_tienda(self):
        with get_session() as session:
            return session.exec(select(Tienda)).all()

    def get_tienda_by_id(self, id:int):
        with get_session() as session:
            return session.exec(select(Tienda).filter(Tienda.id_usuario == id)).first()


    # def create_tienda(self, session: Session, tienda: Tienda):
    #     session.add(tienda)  # Agregar la tienda a la sesión
    #     session.commit()     # Confirmar la transacción
    #     session.refresh(tienda)  # Refrescar los datos de la tienda (si es necesario)
    #     return tienda  # Retornar el objeto tienda persistido