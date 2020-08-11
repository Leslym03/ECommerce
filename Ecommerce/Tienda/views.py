from decimal import Decimal

from django.views.generic import View
from django.shortcuts import render

from Ecommerce.libs.dominio_event import DomainEvents

from Tienda.Dominio.Entidades.producto import Producto
from Tienda.Dominio.Repositorio.compra_repositorio import CompraRepositorio
from Tienda.Dominio.Repositorio.producto_repositorio import ProductoRepositorio
from Tienda.Dominio.Eventos.compra_completa import CompraCompleta
from Tienda.Dominio.factories.compra_factory import CompraFactory


class CompraView(View):

    def get(self, request):
        repository = CompraRepositorio()
        compras = repository.all()
        return render(request, 'compra/lista_compra.html', {'compras': compras})

    def post(self, request):

        cliente_id = 1  # FAKE
        producto_id = request.POST['producto_id']

        compra = CompraFactory.create(cliente_id, producto_id)

        CompraRepositorio().save(compra)

        return render(request, 'compra/terminar_compra.html')


class ProductView(View):

    def get(self, request):
        return render(request, 'producto/nuevo_producto.html')

    def post(self, request):

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = Decimal(request.POST['precio'])

        producto = Product(nombre, descripcion, precio)

        repository = ProductoRepositorio()
        repository.save(producto)

        return render(request, 'producto/nuevo_producto.html')


class TiendaView(View):

    def get(self, request):

        products = ProductRepository().all()

        return render(request, 'tienda/tienda_home.html', {'products': products})
