from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

def base(request):
    return render(request, 'base.html', {})

def index(request):
    return render(request, 'index.html', {})

def vigilancia(request):
    usuarios = list(Usuarios.objects.all())
    departamentos = list(Departamentos.objects.all())
    camaras = list(Camaras.objects.all())
    
    formDepartamentos = Departamentos_Form(request.POST or None, request.FILES or None)
    formCamaras = Camaras_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if formDepartamentos.is_valid():
            formDepartamentos.save()
    if request.method == "POST":
        if formCamaras.is_valid():
            formCamaras.save()

    return render(request, 'vigilancia.html', {"formDepartamentos":formDepartamentos, "formCamaras":formCamaras, "usuarios":usuarios, "departamentos":departamentos, "camaras":camaras})

class SignUp(FormView):
    template_name = 'registrarse.html'
    form_class = Usuarios_Form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        u = Usuarios()
        u.Usuario = user
        u.Nombre = form.cleaned_data['Nombre']
        u.ApellidoP = form.cleaned_data['ApellidoP']
        u.ApellidoM = form.cleaned_data['ApellidoM']
        u.Departamento = form.cleaned_data['Departamento']
        u.TipoUsuario = form.cleaned_data['TipoUsuario']
        u.RFC = form.cleaned_data['RFC']
        u.Domicilio = form.cleaned_data['Domicilio']
        u.Celular = form.cleaned_data['Celular']
        u.Correo = form.cleaned_data['Correo']
        u.Sexo = form.cleaned_data['Sexo']
        u.save()

        return super(SignUp, self).form_valid(form)
