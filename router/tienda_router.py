from fastapi import APIRouter, Depends, HTTPException
from schemas.error_response import error_responses
from schemas.tienda_schema import TiendaReponse, TiendaRequest
from services.tienda_service import get_tienda, create_tienda


router = APIRouter(prefix="/tiendas", tags=["Tiendas"])

@router.get("/all_tiendas", responses=error_responses, response_model=list[TiendaReponse], summary='create_tienda')
def read_tienda(): 
    return get_tienda()

@router.post("/create_tienda", responses=error_responses, response_model=TiendaReponse, summary='create_tienda')
async def agregar_tienda(data_tienda: TiendaRequest):
    return create_tienda(data_tienda)