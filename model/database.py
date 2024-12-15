# database.py
from sqlmodel import create_engine, Session
from os import getenv
from contextlib import contextmanager

DB_URL = getenv("DB_URL", '')

engine = create_engine(
    DB_URL, 
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=60
)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()