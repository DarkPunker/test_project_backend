from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Cliente(SQLModel, table=True):
    C_C: int = Field(primary_key=True)
    Nombre: str
    Apellido: str

class Comentario(SQLModel, table=True):
    id: int = Field(primary_key=True)
    Coment: str
    CC_Cliente: int = Field(foreign_key="cliente.C_C")

class Tienda(SQLModel, table=True):
    Id: int = Field(primary_key=True)
    Nombre: str
    Redes: str
    Celular: str
    Direccion: str

class Categoria(SQLModel, table=True):
    ID_Categoria: int = Field(primary_key=True)
    Nombre: str
    ID_Tienda: int = Field(foreign_key="tienda.Id")

class Producto(SQLModel, table=True):
    Id: int = Field(primary_key=True)
    Nombre: str
    Característica: str
    Descripción: str
    Precio: float
    Stock: int
    ID_Categoria: int = Field(foreign_key="categoria.ID_Categoria")
    ID_comentario: Optional[int] = Field(foreign_key="comentario.id")
