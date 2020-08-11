# Florería Dulces Detalles
<p align="center">
  <img width="30%" height="30%" src="doc/imgs/logo_tienda.png">
</p>

## Integrantes
- Kemely Castillo Caccire
- Lesly Mita Yagua
- Jerson Zúñiga Coayla

## Requisitos
- `python3`

## Configuración
### Usando y activando un entorno virtual
```shell
python -m venv venv
. venv/bin/activate
```
### Instalando requisitos de desarrollo
```shell
pip install -r requirements
```

<p align="center">
  <img width="50%" height="50%" src="doc/imgs/logo_tienda-animado.gif">
</p>

## Prácticas de Codificación
Este proyecto sigue la guía de estilo [PEP 8](https://www.python.org/dev/peps/pep-0008/) para código en Python.

Podemos automatizar y chequear las convenciones de código usando herramientas como [pycodestyle](https://github.com/PyCQA/pycodestyle) y verificar si cumple con las recomendaciones para luego aplicar cambios de forma automática con [autopep8](https://github.com/hhatto/autopep8).

### Verificando convención de estilo según PEP8
Mostrando la primera ocurrencia de cada error
```shell
pycodestyle --first ./path/to/file
```
![Usando pycodestyle](doc/imgs/pycodestyle.png)

### Aplicando correcciones con autopep8
```shell
autopep8 --in-place ./path/to/file
```
![Usando autopep8](doc/imgs/autopep8.png)

## Estilos de Programación
- Pipeline
```python
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
```
- Objects
```python
class Direccion(object):

    def __init__(self, calle, numbero, distrito):
        self.calle = calle
        self.numbero = numbero
        self.distrito = distrito
```
- Trinity
Debido a que se utiliza MVT

## Principios SOLID
### Single Responsibility Principle (SRP)
```python
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

        return Compra(producto, cliente)

### Interface Segregation
```python
def home(request):
    return render(request, 'core/home.html')
def contacto(request):
    return render(request, 'core/contacto.html')
def tienda(request):
    flores = Flor.objects.all()
    return render(request, 'core/tienda.html', {'flores':flores})
```
### Dependency Inversion Principle (DIP)
```python
```
## Domain Driven Design
- Ubiquitous Language
```python
    def nueva_direccion_envio(self, calle, numbero, distrito):
        self.direccion_envio = Direccion(calle, numbero, distrito)
```
- Capas de la arquitectura
Modelo - Vista - Template

- Entities
```python
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

```
- Value Objects
```python

class Nombre(object):  # value object

    def __init__(self, nombres, apellidos, prefix='Sr'):
        self.nombres = nombres
        self.apellidos = apellidos
        self.prefix = prefix

    @property
    def full(self):
        return self.nombre + self.apellido

```
- Services
```python
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
```
- Modules
Compra, producto, cliente
- Aggregates
```python
class Direccion(object):

    def __init__(self, calle, numbero, distrito):
        self.calle = calle
        self.numbero = numbero
        self.distrito = distrito
```
- Factories
```python
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

```
- Repository
```python
class CompraRepositorio(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Compra, CompraData)

    def all(self):
        return CompraData.objects.all()

    def save(self, order):
        compra_data = self.mapper.map(compra, CompraData)
        compra_data.save()

```
