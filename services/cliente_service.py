from model.cliente_model import Cliente
from model.usuario_model import Usuario
from repository.cliente_repository import Cliente_repository
from repository.usuario_repository import Usuario_repository
from schemas.cliente_schema import ClienteCreateRequest, ClienteSchema
from schemas.usuario_schema import TokenUsuarioResponse
from services.usuario_service import create_access_token

_usuario_repository = Usuario_repository()
_cliente_repository = Cliente_repository()

def get_cliente_by_id(id: int):
    return _cliente_repository.get_cliente_by_id(id)

def create_cliente(cliente: ClienteCreateRequest):
    newuser = Usuario(
        email= cliente.email,
        contrasena= cliente.contrasena
    )
    user = _usuario_repository.create_usuario(newuser)
    newcliente = Cliente(
        cc= cliente.cc,
        nombre= cliente.nombre,
        apellido= cliente.apellido,
        direccion= cliente.direccion,
        lat= cliente.lat,
        long= cliente.long,
        id_usuario= user.id,
    )
    client = _cliente_repository.create_cliente(newcliente)
    token = create_access_token({"sub": user.email})
    clienteShem = ClienteSchema.from_orm(client)
    return TokenUsuarioResponse(
        token=token,
        email= user.email,
        cliente= clienteShem,
        tienda=None
    )
    