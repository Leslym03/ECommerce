from direccion import Direccion


class Cliente(object):

    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = Nombre(nombre, apellido)
        self.direccion_envio = None

    def nueva_direccion_envio(self, calle, numbero, distrito):
        self.direccion_envio = Direccion(calle, numbero, distrito)

    @property
    def vip(self):
        # ...
        return True


class Nombre(object):  # value object

    def __init__(self, nombres, apellidos, prefix='Sr'):
        self.nombres = nombres
        self.apellidos = apellidos
        self.prefix = prefix

    @property
    def full(self):
        return self.nombre + self.apellido
