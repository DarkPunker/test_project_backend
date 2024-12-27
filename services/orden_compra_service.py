from model.orden_compra_model import OrdenCompra
from repository.orden_compra_repository import Orden_Compra_repository


_orden_compra_repository = Orden_Compra_repository()

def get_orden_compra_by_cliente(cc_cliente: int):
    return _orden_compra_repository.get_orden_compra_by_cliente(cc_cliente)

def get_orden_compra_by_tienda_producto(id_tienda_producto: int):
    return _orden_compra_repository.get_orden_compra_by_tienda_producto(id_tienda_producto)

def create_orden_compra(orden: OrdenCompra):
    return _orden_compra_repository.create_orden_compra(orden)

def edit_orden_compra(orden: OrdenCompra):
    return _orden_compra_repository.edit_orden_compra(orden)
