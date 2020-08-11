from Tienda.Dominio.Entidades.cliente import Cliente


class ClienteRepositorio(object):

    def get(self, cliente_id):
        # FAKE CLIENT
        cliente = Client(12312312, 'John', 'Smith')
        cliente.id = 1
        return cliente
