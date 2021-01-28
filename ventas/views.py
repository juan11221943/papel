from django.shortcuts import render, redirect
from ventas.forms import VentaForm, productForm
from ventas.models import venta
from inventario.models import Producto
import datetime
from django.db.models import Sum
from time import gmtime, strftime, localtime
import datetime
import os

# Create your views here.

def gananciaDiaria(request):
	vende = venta.objects.all().order_by('fecha')
	bandera = False
	current = None
	lista = []
	contt = 0
	contg = 0
	cont = 0
	aux = [0,0,0]
	for i in vende:
		if bandera == False:
			lista.append([0,0,0])
			current = i.fecha.day
			bandera = True
		if current == i.fecha.day:
			lista[cont][0] = current
			lista[cont][1] += i.total
			lista[cont][2] += i.ganancia
		else:
			lista.append([0,0,0])
			cont += 1
			current = i.fecha.day
			lista[cont][0] = current
			lista[cont][1] += i.total
			lista[cont][2] += i.ganancia
	contexto = {'diario':lista}
	return render(request, 'diario.html', contexto)

def sales(request):
	if request.method == 'POST':
		form = VentaForm(request.POST)
		if form.is_valid():
			suma = venta.objects.aggregate(s = Sum('total'))
			suma1 = venta.objects.aggregate(s = Sum('ganancia'))
			instance = form.save(commit=False)
			instance.fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
			instance.precio = instance.producto.precio_venta
			instance.total = instance.producto.precio_venta * instance.cantidad
			p = Producto.objects.get(id=instance.producto.id)
			aux = p.cantidad
			p.cantidad = aux - instance.cantidad
			p.save()
			instance.ganancia = (instance.producto.precio_venta * instance.cantidad) - (instance.producto.precio_compra * instance.cantidad)
			if suma['s'] == None:
				instance.total_parcial = (instance.producto.precio_venta * instance.cantidad)
				instance.total_ganancia = instance.ganancia
			else:
				instance.total_parcial = suma['s'] + (instance.producto.precio_venta * instance.cantidad)
				instance.total_ganancia = suma1['s'] + instance.ganancia
			instance.save()
		return redirect('listav')
	else:
		form = VentaForm()
	return render(request, 'ventas.html',{'form':form})


def ventasList(request):
	form = productForm()
	vende = venta.objects.all().order_by('fecha')
	contexto = {'ventas':vende, 'form':form}
	if(request.GET.get('mybtn')):
		d = datetime.date.today()
		s = "c:/users/Luz Maritza/Desktop/ventas mes "+str(d.month)+".xls"
		file = open(s, "w")
		file.write("Id Venta\tFecha\tProducto\tCantidad\tPrecio\tTotal\tGanancia\tTotal Parcial\tTotal Ganancia\n")
		for i in vende:
			s = str(i.id) + "\t"+ str(i.fecha) + "\t" + i.producto.nombre + "\t" + str(i.cantidad) + "\t" + str(i.precio) + "\t" + str(i.total) + "\t" + str(i.ganancia) + "\t" + str(i.total_parcial) + "\t" + str(i.total_ganancia) +"\n"
			file.write(s)
		file.close()
		return redirect('listain')
	return render(request, 'listaventas.html', contexto)

def ventaEdit(request, id_venta):
	vende = venta.objects.get(id=id_venta)
	vende1 = venta.objects.get(id=id_venta)
	ganancia = vende.ganancia
	total = vende.total
	vende2 = venta.objects.all().order_by('fecha')
	bandera = False
	if request.method == 'GET':
		form = VentaForm(instance=vende)
	else:
		form = VentaForm(request.POST, instance = vende)
		if form.is_valid():
			for i in vende2:
				if i.id == id_venta:
					bandera = True
				elif bandera == True:
					i.total_parcial -= total
					i.total_ganancia -= ganancia
					i.save()
			suma = venta.objects.aggregate(s = Sum('total'))
			suma1 = venta.objects.aggregate(s = Sum('ganancia'))
			instance = form.save(commit=False)
			instance.fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
			instance.precio = instance.producto.precio_venta
			instance.total = (instance.producto.precio_venta * instance.cantidad)
			p = Producto.objects.get(id=instance.producto.id)
			aux = p.cantidad
			p.cantidad = aux - instance.cantidad + vende1.cantidad
			p.save()
			instance.ganancia = (instance.producto.precio_venta * instance.cantidad) - (instance.producto.precio_compra * instance.cantidad)
			if suma['s'] == None:
				instance.total_parcial = (instance.producto.precio_venta * instance.cantidad)
				instance.total_ganancia = instance.ganancia
			else:
				instance.total_parcial = suma['s'] + (instance.producto.precio_venta * instance.cantidad) - vende1.total
				instance.total_ganancia = suma1['s'] + instance.ganancia - vende1.ganancia
			instance.save()
		return redirect('listav')
	return render(request, 'ventas.html', {'form':form})

def ventaBorr(request, id_venta):
	vende = venta.objects.get(id=id_venta)
	ganancia = vende.ganancia
	total = vende.total
	vende2 = venta.objects.all().order_by('fecha')
	bandera = False
	if request.method == 'POST':
		for i in vende2:
			if i.id == id_venta:
				bandera = True
			elif bandera == True:
				i.total_parcial -= total
				i.total_ganancia -= ganancia
				i.save()
		p = Producto.objects.get(id=vende.producto.id)
		p.cantidad += vende.cantidad
		p.save()
		vende.delete()
		return redirect('listav')
	return render(request, 'ventas_delete.html', {'vende':vende})