from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from MyApp.models import Producto, Comprador, Vendedor, Empresa
# from MyApp.forms import CursoFormulario, ProfesorFormulario

def inicio(request):
        return render(request,"inicio.html")

def producto(request):
    producto =  Producto(nombre="", precio="")
    producto.save()
    documentoDeTexto = f"--->Nombre: {producto.nombre}   Marca: {producto.marca}  Modelo: {producto.modelo} Precio: {producto.precio} Antiguedad: {producto.antiguedad}"

def compradores(request):

      return render(request, "compradores.html")    

def vendedores(request):

      return render(request, "vendedores.html")

def empresas(request):

      return render(request, "empresas.html")


#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

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

from MyApp.forms import UserRegisterForm

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, "inicio.html")



#@login_required
#def estudiantes(request):

    #return render(request, "estudiantes.html")

