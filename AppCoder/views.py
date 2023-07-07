from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario

# Create your views here.

def curso (self):
    curso=Curso(nombre='Desarrollo web', camada='18895')
    curso.save()

    documentoDeTexto=f'El curso es umuy bueno y se llama {curso.nombre}, y la camada es {curso.camada}'
    return HttpResponse (documentoDeTexto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario (request.POST) #aca llega la infomación del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data #Genero un diccionario limpito con la información que necesito
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render (request, 'inicio.html') #Si es POST, que me lleve al inicio
    else:
            miFormulario=CursoFormulario() #Formulario vacio 

    return render(request, 'AppCoder/cursos.html', {"miFormulario": miFormulario}) #si no es POST me quedo acá

def profesorFormulario(request):
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

            return render(request, 'inicio.html')
        
    else:
            miFormulario=ProfesorFormulario()

    return render(request, 'AppCoder/profesorFormulario.html', {'miFormulario': miFormulario})


def busquedaCamada(request):
     return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    if request.GET["camada"]:
          #respuesta=f'Estoy buscando la Camada nro.: {request.GET["camada"]}'
          camada=request.GET['camada']
          curso=Curso.objects.filter(camada__icontains=camada)

          return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': curso, 'camada': camada})
    else:  
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)
            


