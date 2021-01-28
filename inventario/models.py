from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length = 50)
	cantidad = models.IntegerField()
	precio_compra = models.IntegerField()
	precio_venta = models.IntegerField()

	def __str__(self):
		return '{}, precio: {}'.format(self.nombre, self.precio_venta)

	class Meta:
		ordering = ['nombre']