from django import forms
from ventas.models import venta

class VentaForm(forms.ModelForm):
	class Meta:
		model = venta

		fields = [
			'producto', 
			'cantidad',

		]
		labels = {
			'producto' : 'Producto',
			'cantidad' : 'Cantidad',
		}
		widgets = {
			'producto': forms.Select(attrs={'class':'form-control'}),
			'cantidad': forms.TextInput(attrs={'class':'form-control'}),
		}

class productForm(forms.ModelForm):
	class Meta:
		model = venta

		

		fields = [
			'producto', 

		]
		labels = {
			'producto' : '',
		}
		widgets = {
			'producto': forms.Select(attrs={'class':'form-control'}),
		}