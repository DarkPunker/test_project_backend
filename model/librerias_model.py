from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


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