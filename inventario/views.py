from django.shortcuts import render, redirect
from inventario.forms import InventarioForm
from inventario.models import Producto
# Create your views here.
def inven(request):
	if request.method == 'POST':
		form = InventarioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('sale')
	else:
		form = InventarioForm()

	return render(request, 'inventario.html',{'form':form})
	

def invenList(request):
	inven = Producto.objects.all().order_by('cantidad')
	contexto = {'inven':inven, }
	return render(request, 'listainven.html', contexto)