from pydantic import BaseModel

class TiendaSchema(BaseModel):
    id: int
    nombre: str
    redes: str
    celular: int
    direccion: str
    lat: str
    long: str