
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Comentario(SQLModel, table=True):
    __tablename__ = "comentario"
    id: int = Field(primary_key=True)
    coment: str
    cc_cliente: int = Field(foreign_key="cliente.C_C")
