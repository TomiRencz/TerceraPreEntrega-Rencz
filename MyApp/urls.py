from django.urls import path
from MyApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('/vendedor', views.vendedores, name="Vendedores"),
    path('/comprador', views.compradores, name="Compradores"),
    path('/producto', views.producto, name="Productos"),
    path('/empresa', views.empresas, name="Empresas"),
    path('/login', views.login_request, name="Login"),
    path('/register', views.register, name='Register'),
    path('/logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
]