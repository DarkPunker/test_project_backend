from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    unidad_medida: str
    id_categoria: int

    class Config:
        from_attributes = True

class TiendaProductoRequest(BaseModel):
    precio: int
    calificacion: float
    stock: float
    caracteristicas: str
    descripcion: str
    id_tienda: int
    id_producto: int

class TiendaProductoResponse(BaseModel):
    id: int
    precio: int
    calificacion: float
    stock: float
    caracteristicas: str
    descripcion: str
    id_tienda: int 
    id_producto: int 

    model_config = {
        "from_attributes": True 
    }

class TiendaSchema(BaseModel):
    id: int
    nombre: str
    redes: str
    celular: int
    direccion: str
    lat: str
    long: str

class TiendaRequest(BaseModel):
    nombre: str
    redes: str
    celular: int
    direccion: str
    lat: str
    long: str
    email: str

class TiendaReponse(BaseModel):
    id: int
    nombre: str
    redes: str
    celular: int
    direccion: str
    lat: str
    long: str

    class Config:
        from_attributes = True