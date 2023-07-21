from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from AppCoder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
   # path('cursoFormulario/', views.cursoFormulario, name='CursoFormulario'),
   # path('estudianteFormulario/', views.estudianteFormulario, name='EstudianteFormulario'),
   # path('entregableFormulario/', views.entregableFormulario, name='EntregableFormulario'),
    path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    path( 'leerProfesores/', views.leerProfesores, name='LeerProfesores'),
    path ( 'eliminarProfesor/<profesor_nombre>', views.eliminarProfesor, name='EliminarProfesor'),
    path ( 'editarProfesor/<profesor_nombre>', views.editarProfesor, name='EditarProfesor'),
    path ('curso/list', views.CursoList.as_view(), name='List'),
    path (r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path (r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path (r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path (r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    #path ('editar/<int:pk>/', views.CursoUpdate.as_view(), name = 'Edit'),
    #path ('borrar/<int:pk>/', views.CursoDelete.as_view(), name = 'Delete'),
    path( 'login', views.login_request, name='Login'),
    path ('register', views.register, name = "Register"),
    path ('logout', LogoutView.as_view (template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
]

#Manejo de imagenes
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
