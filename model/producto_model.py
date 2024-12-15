from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Producto(SQLModel, table=True):
    __tablename__ = "producto"
    id: int = Field(primary_key=True)
    nombre: str
    unidad_medida: Optional[str]
    id_categoria: Optional[int] = Field(foreign_key="categoria.id")