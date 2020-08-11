from django.db import models


class ProductoData(models.Model):

    class Meta:
        db_table = 'catalog_producto'

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)


class CompraData(models.Model):

    class Meta:
        db_table = 'compra'

    producto_id = models.IntegerField()
    cliente_id = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
