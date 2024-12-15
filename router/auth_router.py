from fastapi import APIRouter, Depends, HTTPException
from schemas.error_response import error_responses
from schemas.usuario_schema import TokenUsuarioResponse, TokenRequest
from services.usuario_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post('/login', responses=error_responses, response_model=TokenUsuarioResponse, summary='Login')
async def login(user_cred: TokenRequest):
    return authenticate_user(user_cred.email, user_cred.contrasena)
    