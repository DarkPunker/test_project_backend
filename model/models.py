from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"
    CC: int = Field(primary_key=True)
    Nombre: str
    Apellido: str

class Comentario(SQLModel, table=True):
    __tablename__ = "comentario"
    id: int = Field(primary_key=True)
    Coment: str
    CC_Cliente: int = Field(foreign_key="cliente.C_C")

class Tienda(SQLModel, table=True):
    __tablename__ = "tienda"
    Id: int = Field(primary_key=True)
    Nombre: str
    Redes: str
    Celular: str
    Direccion: str

class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    ID_Categoria: int = Field(primary_key=True)
    Nombre: str
    ID_Tienda: int = Field(foreign_key="tienda.Id")

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


class Librerias(SQLModel, table=True):
    __tablename__ = "librerias"
    id: int = Field(primary_key=True)
    key: int
    valor: str
    tp_libreria: str

class CamposDeFormularios(SQLModel, table=True):
    __tablename__ = "campos_de_formularios"
    id: int = Field(primary_key=True, default=None)  
    nombre: str
    tipo: str
    formato: str
    libreria: str
    nombre_letrero: str
    isEnable: int
    