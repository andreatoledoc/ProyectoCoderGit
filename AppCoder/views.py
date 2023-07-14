from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario



# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario (request.POST) #aca llega la infomación del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data #Genero un diccionario limpito con la información que necesito
            curso = Curso(nombre=informacion['nombre'], 
                          camada=informacion['camada'])

            
            curso.save()
        return render (request, 'AppCoder/inicio.html') #Si es POST, que me lleve al inicio
    else:
        miFormulario=CursoFormulario() #Formulario vacio 

    return render(request, 'AppCoder/cursos.html', {"miFormulario": miFormulario}) #si no es POST me quedo acá



def profesores(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            profesor = Profesor (nombre = informacion['nombre'], 
                                 apellido=informacion['apellido'], 
                                 email=informacion['email'], 
                                 profesion=informacion['profesion'])
            profesor.save()
        return render(request, 'AppCoder/inicio.html') 
    else:
        miFormulario=ProfesorFormulario()

    return render(request, 'AppCoder/profesores.html', {'miFormulario': miFormulario})


def estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            estudiante = Estudiante (nombre = informacion['nombre'], 
                                 apellido=informacion['apellido'], 
                                 email=informacion['email'])
            estudiante.save()
        return render(request, 'AppCoder/inicio.html') 
    else:
        miFormulario=EstudianteFormulario()

    return render(request, 'AppCoder/estudiantes.html', {'miFormulario': miFormulario})


def entregables(request):
    if request.method == "POST":
        miFormulario = EntregableFormulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data #limpiamos como obtenemos la información
            entregable = Entregable (nombre = informacion['nombre'], 
                                 fecha_entrega=informacion['fecha_entrega'], 
                                 entregado=informacion['entregado'])
            entregable.save()
        return render(request, 'AppCoder/inicio.html') 
    else:
        miFormulario=EstudianteFormulario()

    return render(request, 'AppCoder/entregables.html', {'miFormulario': miFormulario})


def busquedaCamada(request):
     return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    if request.GET["camada"]:
          #respuesta=f'Estoy buscando la Camada nro.: {request.GET["camada"]}'
          camada = request.GET['camada']
          cursos = Curso.objects.filter(camada__icontains = camada)
          return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:  
        respuesta="No enviaste datos"
            
    return render (request, "AppCoder/resultadosBusqueda.html", {"respuesta": respuesta})


