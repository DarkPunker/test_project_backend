from sqlmodel import select
from model.usuario_model import Usuario
from model.database import get_session

class Usuario_repository:
    def __init__(self):
        pass

    def get_usuario(self, email: str, password: str):
        with get_session() as session:
            return session.exec(select(Usuario).filter(Usuario.email == email, Usuario.contrasena == password)).first()