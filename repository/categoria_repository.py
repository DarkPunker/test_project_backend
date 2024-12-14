from sqlmodel import Session, select
from model.categoria_model import Categoria
from model.database import get_session

class categoria_repository():
    def __init__(self):
        pass
    def get_categoria(self):
        with get_session() as session:
            return session.exec(select(Categoria)).all()

    def create_categoria(session: Session, categoria: Categoria):
        session.add(categoria)
        session.commit()
        session.refresh(categoria)
        return categoria
