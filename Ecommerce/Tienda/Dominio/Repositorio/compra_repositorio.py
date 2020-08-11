from mapper.object_mapper import ObjectMapper

from Tienda.models import CompraData
from Tienda.Dominio.Entidades.compra import Compra


class CompraRepositorio(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Compra, CompraData)

    def all(self):
        return CompraData.objects.all()

    def save(self, order):
        compra_data = self.mapper.map(compra, CompraData)
        compra_data.save()
