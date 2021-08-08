from django.shortcuts import render
from pedidos.models import Productos, Categoria

def home(request):

    return render(request, 'webapp/home.html', {})

def servicios(request):

    return render(request, 'webapp/servicios.html', {})

def productos(request):
    categorias = Categoria.objects.all()
    productos = Productos.objects.all()

    context = {'categorias': categorias, 'productos': productos}
    
    return render(request, 'webapp/productos.html', context )

def profesionales(request):
    
    return render(request, 'webapp/profesionales.html', {})

def contacto(request):
    
    return render(request, 'webapp/contacto.html', {})