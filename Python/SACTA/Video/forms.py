from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Usuarios_Form(UserCreationForm):
    Nombre = forms.CharField(max_length = 50)
    ApellidoP = forms.CharField(max_length = 50)
    ApellidoM = forms.CharField(max_length = 50)
    Departamento = forms.ModelChoiceField(queryset = Usuarios.objects.only('Departamento'))
    TipoUsuario = forms.ChoiceField()
    RFC = forms.CharField(max_length = 13)
    Domicilio = forms.CharField(max_length = 100)
    Celular = forms.IntegerField()
    Correo = forms.EmailField(max_length = 100)
    Sexo = forms.ChoiceField()

class Departamentos_Form(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'

class Camaras_Form(forms.ModelForm):
    class Meta:
        model = Camaras
        fields = '__all__'
