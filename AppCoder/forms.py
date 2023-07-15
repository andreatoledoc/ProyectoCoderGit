from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
