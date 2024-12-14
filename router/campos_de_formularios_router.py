from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.models import CamposDeFormularios
from services.campos_de_formularios_service import get_campos_de_formularios

router = APIRouter(prefix="/campo_De_formulario", tags=["campo de formulario"])

@router.get("/")
def read_campo_de_formulario():
    return get_campos_de_formularios()

# @router.post("/")
# def add_producto(producto: Producto, session: Session = Depends(get_session)):
#     return create_producto(session, producto)
