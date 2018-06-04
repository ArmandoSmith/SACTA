from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
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
    ID_Usuario = models.AutoField(primary_key = True)
    Usuario = models.OneToOneField(User)
    Nombre = models.CharField(max_length = 50)
    ApellidoP = models.CharField(max_length = 50)
    ApellidoM = models.CharField(max_length = 50)
    Departamento = models.ForeignKey('Departamentos', on_delete = models.CASCADE, blank = True)
    TipoUsuario = models.CharField(max_length = 15, choices = tipo_usuario)
    RFC = models.CharField(max_length = 13)
    Domicilio = models.CharField(max_length = 100)
    Celular = models.IntegerField()
    Correo = models.EmailField(max_length = 100)
    Sexo = models.CharField(max_length = 9, choices = sexo)

    def __str__(self):
        return self.Nombre

class Departamentos(models.Model):
    ID_Departamento = models.AutoField(primary_key = True)
    Departamento = models.CharField(max_length = 50)

    def __str__(self):
        return self.Departamento

class Camaras(models.Model):
    ID_Camara = models.AutoField(primary_key = True)
    ID_Usuario = models.ForeignKey('Usuarios', on_delete = models.CASCADE)
    ID_Departamento = models.ForeignKey('Departamentos', on_delete = models.CASCADE)
    Puerto = models.CharField(max_length = 4, default = '0000')

    def __int__(self):
        return self.ID_Camara
