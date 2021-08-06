from django.shortcuts import render

def home(request):

    return render(request, 'webapp/home.html', {})

def servicios(request):

    return render(request, 'webapp/servicios.html', {})

def productos(request):
    
    return render(request, 'webapp/productos.html', {})

def profesionales(request):
    
    return render(request, 'webapp/profesionales.html', {})

def contacto(request):
    
    return render(request, 'webapp/contacto.html', {})