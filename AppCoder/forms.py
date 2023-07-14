from django import forms

#Crearmos una mascara para manejar la infomación que va ingresando
#O sea le vamos dando formato
class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email = forms.EmailField()

class ProfesorFormulario (forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email = forms.EmailField()
    profesion=forms.CharField()

class EntregableFormulario (forms.Form):
    nombre=forms.CharField()
    fecha_entrega = forms.DateField()
    entregado=forms.BooleanField
