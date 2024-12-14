from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Producto(SQLModel, table=True):
    __tablename__ = "producto"
    Id: int = Field(primary_key=True)
    Nombre: str
    Característica: str
    Descripción: str
    Precio: float
    Stock: int
    ID_Categoria: int = Field(foreign_key="categoria.ID_Categoria")
    ID_comentario: Optional[int] = Field(foreign_key="comentario.id")
