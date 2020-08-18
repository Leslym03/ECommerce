<p align="center">
  <img width="50%" height="50%" src="doc/imgs/flores.png">
</p>

---

# Florería Dulces Detalles
Dulces Detalles es una plataforma web que nos va a permitir realizar compras de arreglos de flores basado en una tienda  virtual ,ademas de ofrecer un portal didáctico que permita registrar las personas que ingresen a la página  y realicen su pedido.

<p align="center">
  <img width="30%" height="30%" src="doc/imgs/DulcesDetalles.png">
</p>

### Proposito
Crear un sistema que ayude a incrementar el número de ventas y tener más cercanía con los clientes.
### Funcionalidades
El sistema debe:
- Tener por artículo:
  - Categoría a la que pertenece.
  - Descripción breve.
- Realizar operaciones sobre los pedidos:
  - Modificar, agregar, eliminar y consultar sobre un pedido.
  - Búsqueda de pedidos por cliente.
  - Modificación del estado de un pedido.
### Arquitectura
Posee una organización de los 3 paquetes principales los cuales son vista, modelo y template utilizando el patrón arquitectónico MVT (Modelo Vista Template) en este patrón la vista actuaria como controlador, aunque con pequeños matices esto debido a que se utilizara el Framework Django.

<p align="center">
  <img width="50%" height="50%" src="doc/imgs/esquema.png">
</p>

- **Vista**:la capa de la lógica de negocios.
   - Contiene clases para interactuar con el sistema para realizar una compra, pedido, registro, etc.
- **Template**:la capa de presentación.
   - Contiene clases para cada formularios que los actores usan para comunicarse con el sistema.
- **Modelo**:la capa de acceso a la base de datos.
   - Incluye clases de entidad para los usuarios y clases límite para la interfaz con el sistema de catálogo de productos.



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

### Usando flake8
Con flake8 podemos definir el estilo de programación que la compañía de software usará, teniendo como base las recomendaciones de PEP8. Se definieron las siguientas opciones de configuración:
```shell
max-line-length = 80
per-file-ignores =
    manage.py:F401
show_source = True
count = True
```









## Estilos de Programación
### Pipeline
```python
```
### Objects
```python
```
### Trinity
(Debido a que se utiliza MVT)
```python
```











## Principios SOLID
### Single Responsibility Principle (SRP)
```python
```
### Open Closed Principle (OCP)
```python
```
### Liskov Substitution Principle (LSP)
```python
```
### Interface Segregation Principle (ISP)
```python
```
### Dependency Inversion Principle (DIP)
```python
```








## Conceptos Domain Driven Design (DDD)

### Modules
- **Product**:
- **Order**:
- **Client**:

### Ubiquitous Language:

Se nombraron las variables, métodos y clases con lenguaje del dominio de modo que sea autoexplicable
- ```python new_shipping_address```

### Entities
```python
class Client(object):

    def __init__(self, idClient, name, last_name):
        self.set_idClient(idClient)
        self.name = Name(name, last_name)
        self.shipping_address = None

    def set_idClient(self, idClient):
        self.idClient = idClient

    def get_idClient(self):
        return self.idClient

    def new_shipping_address(self, street, number, city):
        self.shipping_address = Address(street, number, city)
```

### Value Objects
```python
class Name(object):  
    def __init__(self, first, last):
        self.set_first(first)
        self.set_last(last)

    def set_first(self, first):
        self.first = first

    def get_first(self):
        return self.first

    def set_last(self, last):
        self.last = last

    def get_last(self):
        return self.last

    @property
    def full(self):
        return self.name + self.last_name
```

### Aggregates
```python
class Address(object):

    def __init__(self, street, number, city):
        self.set_street(street)
        self.set_number(number)
        self.set_city(city)

    def set_street(self, street):
        self.street = street

    def set_number(self, street):
        self.number = number

    def set_city(self, city):
        self.city = city

    def get_street(self):
        return self.street

    def get_number(self):
        return self.number

    def get_city(self):
        return self.city
```

### Factories
```python
class OrderFactory(object):

    @classmethod
    def create(cls, client_id, product_id):
        client = ClientRepository().get(client_id)
        product = ProductRepository().get(product_id)
        #...
        return Order(product, client)
```

### Repository
```python

class ClientRepository(AbstractDataMapper):

    def find_all(self):
        client_models = ClientModel.objects.all()
        client_entities = []
        for client_model in client_models:
            client_entity = self.__load_entity(client_model)
            client_entities.append(client_entity)
        return client_entities

    def find_by_id(self, id):
        client_model = ClientModel.objects.get(idClient=id)
        client = self.__load_entity(client_model)
        return client

    def create(self, client):
        ClientModel(
            idClient=client.get_idClient(),
            first_name=client.get_first(),
            last_name=client.get_last()
        ).save()

    def update(self, client):
        client_model = ClientModel.objects.get(idClient=client.get_idClient())
        client_model.first_name = client.get_first()
        client_model.last_name = client.get_last()
        client_model.save()

    def delete(self, entity):
        pass

    def __load_entity(self, client_model):
        client_entity = Client(
            client_model.idClient,
            Name(client_model.name)
        )
        return client_entity
```

### Event
```python
class DomainEvents(object):

    def __init__(self):
        pass

    @classmethod
    def trigger(cls, event):

        handlers = set()
        for child in event.__class__.__subclasses__():
            if child not in handlers:
                handlers.add(child)

        for handler in handlers:
            handler_instance = handler()
            handler_instance.run()

class OrderCompletedView(View):
    #....
    client_id = request.POST['client_id']
    product_id = request.POST['product_id']

    order = OrderFactory.created(client_id,product_id)
    OrderRepository().save(order)
    DomainEvents.trigger(OrderCompleted(order))
```





















## Ejecucion del proyecto
### Usando y activando un entorno virtual
```shell
python -m venv venv
. venv/bin/activate
```
### Instalando requisitos de desarrollo
```shell
pip install -r requirements
```

## Integrantes
- Kemely Castillo Caccire
- Lesly Mita Yagua
- Jerson Zúñiga Coayla

---
<p align="center">
  <img width="50%" height="50%" src="doc/imgs/flores.png">
</p>
