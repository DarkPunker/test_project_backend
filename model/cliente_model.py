from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"
    cc: int = Field(primary_key=True)
    nombre: str
    apellido: str
