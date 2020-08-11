class CompraCompleta(object):

    def __init__(self, compra):
        self.compra = compra


class Generar_factura(CompraCompleta):

    def __init__(self):
        pass

    def run(self):
        # regla de factura
        pass


class Eliminar_producto_inventario(CompraCompleta):

    def __init__(self):
        pass

    def run(self):
        # regra para remover o produto
        pass
