from django.db import models
from inventario.models import Producto
# Create your models here.

class venta(models.Model):
	fecha = models.DateTimeField(blank=True,null=True,)
	producto = models.ForeignKey(Producto,blank=True,null=True, on_delete=models.CASCADE,)
	cantidad = models.IntegerField(blank=True,null=True,)
	precio = models.IntegerField(blank=True,null=True,)
	total = models.IntegerField(blank=True,null=True,)
	ganancia = models.IntegerField(blank=True,null=True,)
	total_parcial = models.IntegerField(blank=True,null=True,)
	total_ganancia = models.IntegerField(blank=True,null=True,)

class Efectivo(models.Model):
	Dia = models.IntegerField(blank=True,null=True,)
	efectivo_billete = models.IntegerField(blank=True,null=True,)
	efectivo_moneda = models.IntegerField(blank=True,null=True,)
	def __str__(self):
		return 'Dia: {}, Billete:  {}, Moneda: {}'.format(self.Dia, self.efectivo_billete, self.efectivo_moneda)

