from sqlmodel import Session, select
from model.models import CamposDeFormularios
from model.database import get_session

class campos_de_formularios_repository():
    def __init__(self):
        pass
    def get_campos_de_formularios(self):
        with get_session() as session:
            return session.exec(select(CamposDeFormularios)).all()

    def create_campos_de_formularios(session: Session, campos_de_formularios: CamposDeFormularios):
        session.add(campos_de_formularios)
        session.commit()
        session.refresh(campos_de_formularios)
        return campos_de_formularios
