from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable, Avatar
from django.http import HttpResponse
from AppCoder.forms import AvatarFormulario, UserRegisterForm, CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario, UserEditForm, User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #Me permite que los objetos se carguen background
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

#Login

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'AppCoder/inicio.html', {'url':avatares[0].imagen.url})

'''
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
'''

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contras)

            if user is not None:
                login(request, user)
                return render (request, 'AppCoder/inicio.html', {'mensaje': f"Bienvenido {usuario}"})

            else:
                return render (request, 'AppCoder/inicio.html', {"mensaje": "Error, datos erroneos"})
        else:
            return render (request, 'AppCoder/inicio.html', {'mensaje': 'Error, formulario erroneo'})

    form = AuthenticationForm()

    return render (request, 'AppCoder/login.html', {'form': form})


def register (request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Usuario creado:"})
        
    else:
            form = UserRegisterForm()

    return render (request, "AppCoder/registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user 

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.password1 = informacion['password1']
            usuario.password1 = informacion['password2']
            usuario.save()
 
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'AppCoder/agregarAvatar.html', {'miFormulario':miFormulario})

#Clase propias de la App
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
        miFormulario=EntregableFormulario()

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
            
    return render (request, "AppCoder/inicio.html", {"respuesta": respuesta})


def leerCursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos":cursos}
    return render(request, "AppCoder/leerCursos.html", contexto)

def leerProfesores (request):
    profesores = Profesor.objects.all() #trae todos los profesores
    contexto = {"profesores": profesores}

    return render (request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesor (request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}

    return render (request, 'AppCoder/leerProfesores.html', contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre = profesor_nombre)

    if  request.method == "POST":
        miFormulario = ProfesorFormulario (request.POST)
        print (miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion ['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            return render (request, 'AppCoder/inicio.html')
        
    else:
            miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre,
                                                       'apellido': profesor.apellido,
                                                       'email': profesor.email,
                                                       'profesion': profesor.profesion})
            
    return render (request, 'AppCoder/editarProfesor.html', {'miFormulario': miFormulario, 'profesor_nombre': profesor_nombre})
    

class CursoList(ListView):
    model = Curso
    template_name='AppCoder/curso_list.html'

class CursoDetalle (DetailView):
    model = Curso
    template_name='AppCoder/curso_detalle.html'

class CursoCreacion (CreateView):
    model = Curso
    success_url='AppCoder/curso/list'
    fields = ['nombre', 'camada']

class CursoUpdate (UpdateView):
    model = Curso
    success_url = reverse_lazy('List')
    #success_url='AppCoder/curso/list'
    fields = ['nombre', 'camada']

class CursoDelete (DeleteView):
    model = Curso
    success_url = reverse_lazy('List')
    #success_url='AppCoder/curso/list'

