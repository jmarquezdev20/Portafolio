from django.shortcuts import render
from datetime import datetime

def inicio(request):
    return render(request, 'inicio.html', {'year': datetime.now().year})

def sobre_mi(request):
    return render(request, 'sobre_mi.html', {'year': datetime.now().year})

def proyectos(request):
    return render(request, 'proyectos.html', {'year': datetime.now().year})

def contacto(request):
    enviado = False
    nombre = ""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        enviado = True
    return render(request, 'contacto.html', {'enviado': enviado, 'nombre': nombre, 'year': datetime.now().year})

def certificaciones(request):
    return render(request, 'certificaciones.html', {
        'year': datetime.now().year
    })