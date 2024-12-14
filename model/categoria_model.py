from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    ID_Categoria: int = Field(primary_key=True)
    Nombre: str
    ID_Tienda: int = Field(foreign_key="tienda.Id")
