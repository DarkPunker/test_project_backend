from sqlmodel import SQLModel, Field
from typing import Optional

class TiendaProducto(SQLModel, table=True):
    __tablename__ = "tienda_producto"

    id: Optional[int] = Field(default=None, primary_key=True) 
    precio: Optional[int] = Field(default=None)
    calificacion: Optional[int] = Field(default=None)
    stock: Optional[int] = Field(default=None)
    caracteristica: Optional[str] = Field(default=None, max_length=255)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    id_tienda: int = Field(foreign_key="tienda.id")  
    id_producto: int = Field(foreign_key="producto.id")  
    id_comentario: Optional[int] = Field(default=None)
