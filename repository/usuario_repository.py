from sqlmodel import Session, select
from model.usuario_model import Usuario

class Usuario_repository:
    def __init__(self):
        pass

    def get_usuario(self, session: Session):
        return session.exec(select(Usuario)).all()

    def create_usuario(self, session: Session, usuario: Usuario):
        session.add(usuario)  
        session.commit()   
        session.refresh(usuario)  
        return usuario  