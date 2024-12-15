from sqlmodel import Session, select
from model.usuario_model import Usuario

class Usuario_repository:
    def __init__(self):
        pass

    def get_usuario(self, session: Session):
        return session.exec(select(Usuario)).all()

    def create_usuario(self, session: Session, usuario: Usuario):
        session.add(usuario)  # Agregar la tienda a la sesión
        session.commit()     # Confirmar la transacción
        session.refresh(usuario)  # Refrescar los datos de la tienda (si es necesario)
        return usuario  # Retornar el objeto tienda persistido