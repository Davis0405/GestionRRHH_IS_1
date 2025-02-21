from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import Empleados
from .forms import EmpleadoForm

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
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
def lista_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})

def nuevo_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/form.html', {'form': form})

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleados, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/form.html', {'form': form})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleados, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'empleados/confirmar_eliminar.html', {'empleado': empleado})