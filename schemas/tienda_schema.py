from typing import Optional
from pydantic import BaseModel



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