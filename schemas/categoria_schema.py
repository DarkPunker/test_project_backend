from pydantic import BaseModel


class CategoriaResponse(BaseModel):
    id: int
    nombre: str
    id_tienda: int

    class Config:
        from_attributes = True