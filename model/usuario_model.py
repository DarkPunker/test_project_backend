from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    id: Optional[int] = Field(primary_key=True)
    email: str
    contrasena: str

   