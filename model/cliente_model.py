from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"
    CC: int = Field(primary_key=True)
    Nombre: str
    Apellido: str
