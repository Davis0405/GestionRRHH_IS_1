from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def inicio(request):
    return render(request, 'inicio.html') 
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class CustomLoginView(LoginView):
    template_name = 'rrhh/login.html'
    redirect_authenticated_user = True  # Redirige si el usuario ya está autenticado

    def get_success_url(self):
        return reverse_lazy('dashboard')  # Redirige al dashboard después de iniciar sesión
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirige al login después de cerrar sesión
#-----------------------------------------------------------------------------------------------------------------------------------------------------   
@login_required
def dashboard(request):
    return render(request, 'rrhh/dashboard.html')
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
@login_required
def empleados(request):
    return render(request, 'rrhh/empleados.html')
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
@login_required
def nominas(request):
    return render(request, 'rrhh/nominas.html')
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
@login_required
def prestaciones(request):
    return render(request, 'rrhh/prestaciones.html')
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
@login_required
def reportes(request):
    return render(request, 'rrhh/reportes.html')
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
def custom_logout(request):
    logout(request)
    return redirect('login')