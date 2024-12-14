from sqlmodel import Session, select
from model.cometario_model import Comentario
from model.database import get_session

class comentario_repository():
    def __init__(self):
        pass
    def get_comentario(self):
        with get_session() as session:
            return session.exec(select(Comentario)).all()

    def create_comentario(session: Session, comentario: Comentario):
        session.add(comentario)
        session.commit()
        session.refresh(comentario)
        return comentario
