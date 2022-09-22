from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TipoDocumento
from .forms import TipoDocumentoForm
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def documento(request):
    documento = TipoDocumento.objects.all()
    return render(request,'documento.html',{'documento':documento})

def crear(request):
    formulario = TipoDocumentoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('documento')
    return render(request,'crear.html',{'formulario':formulario})

def editar(request, id):
    documento = TipoDocumento.objects.get(id=id)
    formulario = TipoDocumentoForm(request.POST or None, request.FILES or None, instance = documento )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('documento')
    return render(request,'editar.html' , {'formulario':formulario})

def borrar(request, id):
    documento = TipoDocumento.objects.get(id=id)
    documento.delete()
    return redirect('documento')