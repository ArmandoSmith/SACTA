from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Usuarios_Form(UserCreationForm):
    sexo = (
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
    )
    tipo_usuario = (
        ('Administrador', 'Administrador'),
        ('Gerente General', 'Gerente General'),
        ('Gerente', 'Gerente'),
        ('Supervisor', 'Supervisor'),
        ('Empleado', 'Empleado'),
        ('Outsourcing', 'Outsourcing'),
        ('Practicante', 'Practicante')
    )
    Nombre = forms.CharField(max_length = 50)
    ApellidoP = forms.CharField(max_length = 50)
    ApellidoM = forms.CharField(max_length = 50)
    Departamento = forms.ModelChoiceField(queryset = Departamentos.objects.only('Departamento'))
    TipoUsuario = forms.ChoiceField(choices = tipo_usuario)
    RFC = forms.CharField(max_length = 13)
    Domicilio = forms.CharField(max_length = 100)
    Celular = forms.IntegerField()
    Correo = forms.EmailField(max_length = 100)
    Sexo = forms.ChoiceField(choices = sexo)

class Departamentos_Form(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'

class Camaras_Form(forms.ModelForm):
    class Meta:
        model = Camaras
        fields = '__all__'
