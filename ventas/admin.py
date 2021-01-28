from django.contrib import admin
from ventas.models import venta
from ventas.models import Efectivo
# Register your models here.

admin.site.register(venta)
admin.site.register(Efectivo)