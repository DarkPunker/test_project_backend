from repository.campos_de_formularios import campos_de_formularios_repository

_campo_de_formulario = campos_de_formularios_repository()

def get_campos_de_formularios():
    return _campo_de_formulario.get_campos_de_formularios()