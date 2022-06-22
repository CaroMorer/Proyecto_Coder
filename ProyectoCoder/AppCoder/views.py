from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.
def curso(self):
    curso = Curso(nombre = "Datos", camada = "22")
    curso.save()
    documento_texto = f"--Curso: {curso.nombre}, Camada: {curso.camada}"
    return HttpResponse(documento_texto)


