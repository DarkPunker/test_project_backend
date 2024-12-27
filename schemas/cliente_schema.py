from pydantic import BaseModel, ConfigDict

class ClienteSchema(BaseModel):
    cc: int
    nombre: str
    apellido: str
    direccion: str
    lat: str
    long: str

    model_config = ConfigDict(from_attributes=True)

class ClienteCreateRequest(BaseModel):
    cc: int
    email: str
    contrasena: str
    nombre: str
    apellido: str
    direccion: str
    lat: str
    long: str
