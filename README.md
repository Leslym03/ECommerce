# Floreria TIKA
<p align="center">
  <img width="30%" height="30%" src="imagen/TIKA.png">
</p>

## Integrantes
- Kemely Castillo Caccire
- Lesly Mita Yagua
- Jerson Zúñiga Coayla

## Requisitos
- `python3`
- `Django 3.0.8`

### Usando y activando un entorno virtual
```
python -m venv venv
. venv/bin/activate

```
<p align="center">
  <img width="50%" height="50%" src="imagen/tik.gif">
</p>

## Estilos de Programacion
- Pipeline
- Cookbook
- Trinity

## Principios SOLID
- Interface Segregation
```python
def home(request):
    return render(request, 'core/home.html')
def contacto(request):
    return render(request, 'core/contacto.html')

```
