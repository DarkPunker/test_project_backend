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


    def create_tienda(self, tienda: Tienda):
        print(tienda)
        with get_session() as session:  
            session.add(tienda)      
            session.commit()        
            session.refresh(tienda)   
            return tienda   