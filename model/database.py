# database.py
from sqlmodel import create_engine, Session
from os import getenv

DB_URL = getenv("DB_URL", '')

engine = create_engine(
    DB_URL, 
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=60
)

def get_session() -> Session:
    """Retorna una nueva sesión para ser utilizada en funciones de consulta/operación."""
    return Session(engine)