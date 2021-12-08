from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Data
from .forms import DataForms

def inicio(request):
    try:
        data = Data.objects.all()
        formulario = DataForms(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')        
        return render(request, 'inicio.html', { 'data': data, 'formulario': formulario })
    except Exception as e:
        print('Creacion de alumno incorrecta: ', e)
        
def eliminar(request, id):
    try:
        data = Data.objects.get(id = id)
        data.delete()
        return redirect('inicio')
    except Exception as e:
        print('Opcion no eliminada: ', e)    

def editar(request, id):
    try:
        data = Data.objects.get(id = id)  
        editar = DataForms(request.POST or None, instance = data)  
        if editar.is_valid():
            editar.save()
            return redirect('inicio')
        return render(request, 'editar.html', {'editar': editar })
    except Exception as e:
        print('Opcion a editar no actualizada: ', e)