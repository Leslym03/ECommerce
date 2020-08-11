from mapper.object_mapper import ObjectMapper

from Tienda.models import ProductoData
from Tienda.Dominio.Entidades.producto import Producto


class ProductoRepositorio(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Producto ProductoData)

    def get(self, id):
        o
        producto = Producto(nombre='Fake', descripcion='Fake', precio=11)
        producto.id = 1
        return producto

    def save(self, producto):
        producto_data = self.mapper.map(producto, ProductoData)
        producto_data.save()

    def all(self):
        return ProductoData.objects.all()
