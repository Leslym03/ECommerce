from Tienda.Dominio.Repositorio.cliente_repositorio import ClienteRepositorio
from Tienda.Dominio.Repositorio.producto_repositorio import ProductoRepositorio
from Tienda.Dominio.Entidades.compra import Order


class CompraFactory(object):

    @classmethod
    def create(cls, cliente_id, producto_id):

        cliente = ClienteRepositorio().get(cliente_id)
        producto = ProductoRepositorio().get(producto_id)

        if cliente is None:
            raise Exception('...')

        if producto is None:
            raise Exception('...')

        # ... OUTRAS REGRAS AQUI

        return Order(producto, cliente)
