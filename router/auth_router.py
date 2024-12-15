from fastapi import APIRouter, Depends, HTTPException
from schemas.error_response import error_responses
from schemas.usuario_schema import TokenUsuarioResponse, TokenRequest
from services.usuario_service import authenticate_user
from services.cliente_service import create_cliente
from model.cliente_model import Cliente
from pydantic import BaseModel
from repository.cliente_repository import Cliente_repository

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post('/login', responses=error_responses, response_model=TokenUsuarioResponse, summary='Login')
async def login(user_cred: TokenRequest):
    return authenticate_user(user_cred.email, user_cred.contrasena)



class ClienteCreateRequest(BaseModel):
    nombre: str
    apellido: str
    direccion: str
    lat: str
    long: str
    

@router.post('/create_cliente', response_model=Cliente, summary='Create Cliente')
async def create_new_cliente(cliente: Cliente):
    try:
        new_cliente = create_cliente(cliente)
        return new_cliente
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))