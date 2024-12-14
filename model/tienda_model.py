from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Tienda(SQLModel, table=True):
    __tablename__ = "tienda"
    id: int = Field(primary_key=True)
    nombre: str
    redes: str
    celular: str
    direccion: str