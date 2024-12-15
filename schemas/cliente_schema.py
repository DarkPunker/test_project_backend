from pydantic import BaseModel


class ClienteSchema(BaseModel):
    cc: int
    nombre: str
    apellido: str
    direccion: str
    lat: str
    long: str