from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class OrdenCompra(SQLModel, table=True):
    __tablename__ = "orden_compra"
    id: int = Field(primary_key=True)
    comentario: Optional[str]
    cantidad: Optional[float]
    calificacion: Optional[float]
    estado: Optional[int]
    cc_cliente: Optional[int] = Field(foreign_key="cliente.cc")
    id_tienda_producto: Optional[int] = Field(foreign_key="tienda_producto.id")