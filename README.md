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
- `MySQL 8.0`

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
- Cookbook
- Trinity

## Principios SOLID

### Single Responsibility Principle
```python
class Estado(models.Model):
    nombre_estado = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre_estado

class Flor(models.Model):
    imagen = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=50, primary_key=True)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    stock = models.IntegerField() 

    def __str__(self):
        return self.nombre

```

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
