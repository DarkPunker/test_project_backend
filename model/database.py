from sqlmodel import create_engine
from os import getenv
from sqlmodel import Session
from contextlib import contextmanager

DB_URL = getenv("DB_URL", '')

engine = create_engine(
                        DB_URL, 
                        echo=True,
                        pool_size=10,           # Número de conexiones persistentes en el pool
                        max_overflow=20,        # Número máximo de conexiones adicionales que pueden crearse
                        pool_timeout=60         # Tiempo de espera en segundos para obtener una conexión antes de lanzar TimeoutError  
                    )

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
       session.close()