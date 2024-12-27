from sqlmodel import SQLModel, Field
from typing import Optional

class TiendaProducto(SQLModel, table=True):
    __tablename__ = "tienda_producto"

    id: Optional[int] = Field(primary_key=True)
    precio: Optional[int]
    calificacion: Optional[float]
    stock: Optional[float]
    caracteristicas: Optional[str]
    descripcion: Optional[str]
    id_tienda: int = Field(foreign_key="tienda.id")
    id_producto: int = Field(foreign_key="producto.id")
