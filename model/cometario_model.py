
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Comentario(SQLModel, table=True):
    __tablename__ = "comentario"
    id: int = Field(primary_key=True)
    Coment: str
    CC_Cliente: int = Field(foreign_key="cliente.C_C")
