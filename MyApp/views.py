from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from MyApp.models import Producto, Comprador, Vendedor, Empresa
from MyApp.forms import *
# from MyApp.forms import CursoFormulario, ProfesorFormulario

def inicio(request):
        return render(request,"inicio.html")

def producto(request):
      if request.method == 'POST':
            miFormulario = ProductoFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Producto(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio'],antiguedad=informacion['antiguedad']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= CompradorFormulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def compradores(request):
      if request.method == 'POST':
            miFormulario = CompradorFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  comprador = Comprador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
                  comprador.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= CompradorFormulario() 
      return render(request, "compradores.html", {"miFormulario":miFormulario}) 

def vendedores(request):
      if request.method == 'POST':
            miFormulario = VendedorFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  vendedor = Vendedor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
                  vendedor.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= VendedorFormulario() 
      return render(request, "vendedores.html", {"miFormulario":miFormulario})

def empresas(request):
      if request.method == 'POST':
            miFormulario = EmpresasFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  empresa = Empresa(nombre=informacion['nombre']) 
                  empresa.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= EmpresasFormulario() 
      return render(request, "empresas.html", {"miFormulario":miFormulario}) 

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre'] 
        productos = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "inicio.html", {"productos":productos, "nombre":nombre})
    else: 
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, "inicio.html")

