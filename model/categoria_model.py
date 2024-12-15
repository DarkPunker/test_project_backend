from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    id: int = Field(primary_key=True)
    nombre: str
    id_tienda: Optional[int] = Field(foreign_key="tienda.id")