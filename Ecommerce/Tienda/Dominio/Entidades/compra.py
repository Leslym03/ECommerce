class Compra(object):

    def __init__(self, producto, client):
        self.producto_id = producto.id
        self.cliente_id = cliente.dni
        self.precio = producto.precio

        if client.vip:
            self.precio = self.vip_descuento()

    def vip_descuento(self):
        self.precio -= self.precio * 0.09
        return self.precio

    def cancel():
        pass
        # .....
