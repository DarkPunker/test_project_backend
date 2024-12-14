from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Tienda(SQLModel, table=True):
    __tablename__ = "tienda"
    Id: int = Field(primary_key=True)
    Nombre: str
    Redes: str
    Celular: str
    Direccion: str