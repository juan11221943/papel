from django import forms
from inventario.models import Producto

class InventarioForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields = [
			'nombre', 
			'cantidad',
			'precio_compra',
			'precio_venta',

		]
		labels = {
			'nombre' : 'Nombre',
			'cantidad' : 'Cantidad',
			'precio_compra' : 'Precio compra',
			'precio_venta' : 'Precio venta',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'cantidad': forms.TextInput(attrs={'class':'form-control'}),
			'precio_compra': forms.TextInput(attrs={'class':'form-control'}),
			'precio_venta': forms.TextInput(attrs={'class':'form-control'}),

		}