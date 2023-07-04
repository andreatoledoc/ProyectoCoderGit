from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def curso (self):
    curso=Curso(nombre='Desarrollo web', camada='18895')
    curso.save()

    documentoDeTexto=f'El curso es {curso.nombre}, y la camada {curso.camada}'
    return HttpResponse (documentoDeTexto)
