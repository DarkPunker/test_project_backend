from typing import Optional
from pydantic import BaseModel

from schemas.cliente_schema import ClienteSchema
from schemas.tienda_schema import TiendaSchema

class TokenRequest(BaseModel):
    email: str
    contrasena: str

class TokenUsuarioResponse(BaseModel):
    token: str
    email: str
    cliente: ClienteSchema
    tienda: Optional[TiendaSchema]

    class Config:
        from_attributes = True

class UsuarioSchema(BaseModel):
    email: str
    contrasena: str