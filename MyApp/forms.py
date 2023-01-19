from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VendedorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()  

class CompradorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()  

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    antiguedad = forms.IntegerField()

class EmpresasFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}