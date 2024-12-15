from repository.usuario_repository import Usuario_repository
from model.usuario_model import Usuario
from sqlmodel import Session  # Importa Session

_usuario_repository = Usuario_repository()

def get_usuario(session: Session):
    return _usuario_repository.get_usuario(session)

def create_usuario(session: Session, tienda: Usuario):
    return _usuario_repository.create_usuario(session, Usuario)