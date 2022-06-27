from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from AppCoder.models import Curso
# Create your views here.
def curso(request):
    curso = Curso(nombre = "Datos", camada = "22")
    curso.save()
    curso2 = Curso(nombre="Marketing", camada="247")
    curso2.save()

    documento_texto = f"--Curso1: {curso.nombre}, Camada: {curso.camada}, ---Curso2: {curso2.nombre} Camada: {curso2.camada}"
    return HttpResponse(documento_texto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
