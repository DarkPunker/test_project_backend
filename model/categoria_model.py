from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    id_categoria: int = Field(primary_key=True)
    nombre: str
    id_tienda: int = Field(foreign_key="tienda.Id")
