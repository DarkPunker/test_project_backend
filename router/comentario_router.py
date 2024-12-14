from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.cometario_model import Comentario
from services.comentario_service import get_comentario

router = APIRouter(prefix="/comentario", tags=["Comentario"])

@router.get("/")
def read_comentario():
    return get_comentario()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
