from fastapi import HTTPException
from repository.usuario_repository import Usuario_repository
from repository.cliente_repository import Cliente_repository
from repository.tienda_repository import Tienda_repository
from schemas.cliente_schema import ClienteSchema
from schemas.tienda_schema import TiendaSchema
from schemas.usuario_schema import TokenUsuarioResponse

import jwt
from datetime import datetime, timedelta
from os import getenv

_usuario_repository = Usuario_repository()
_cliente_repository = Cliente_repository()
_tienda_repository = Tienda_repository()


def authenticate_user(email: str, password: str):
    user = _usuario_repository.get_usuario(email, password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    client = _cliente_repository.get_cliente_by_id(user.id)
    tiend = _tienda_repository.get_tienda_by_id(user.id)

    print(client)

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado",
        )
    
    token = create_access_token({"sub": user.email})
    return TokenUsuarioResponse(
        token=token,
        email=user.email,
        cliente=ClienteSchema(
            cc= client.cc,
            nombre= client.nombre,
            apellido= client.apellido,
            direccion= client.direccion,
            lat= client.lat,
            long= client.long),
        tienda=TiendaSchema(
            id= tiend.id,
            nombre= tiend.nombre,
            redes= tiend.redes,
            celular= tiend.celular,
            direccion= tiend.direccion,
            lat= tiend.lat,
            long= tiend.long
        ) if tiend else None,
    )

def create_access_token(data: dict, expires_delta: timedelta = timedelta(weeks=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, getenv("SECRET_KEY", ''), algorithm="HS256")
    return encoded_jwt