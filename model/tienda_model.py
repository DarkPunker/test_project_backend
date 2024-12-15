from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Tienda(SQLModel, table=True):
    __tablename__ = "tienda"
    id: int = Field(primary_key=True)
    nombre: str
    redes: Optional[str]
    celular: Optional[int]
    direccion: Optional[str]
    lat: Optional[str]
    long: Optional[str]
    id_usuario: int = Field(foreign_key="usuario.id")