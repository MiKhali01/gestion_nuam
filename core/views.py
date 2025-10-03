from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa
from django.http import JsonResponse

# Listado de empresas (HTML + JSON)


def lista_empresas(request):
    empresas = Empresa.objects.all()
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse(list(empresas.values()), safe=False)
    return render(request, "lista_empresas.html", {"empresas": empresas})

# Crear empresa


def crear_empresa(request):
    if request.method == "POST":
        Empresa.objects.create(
            nombre=request.POST["nombre"],
            pais=request.POST["pais"],
            identificador=request.POST["identificador"]
        )
        return redirect("lista_empresas")
    return render(request, "crear_empresa.html")

# Editar empresa


def editar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    if request.method == "POST":
        empresa.nombre = request.POST["nombre"]
        empresa.pais = request.POST["pais"]
        empresa.identificador = request.POST["identificador"]
        empresa.save()
        return redirect("lista_empresas")
    return render(request, "editar_empresa.html", {"empresa": empresa})

# Eliminar empresa


def eliminar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresa.delete()
    return redirect("lista_empresas")
