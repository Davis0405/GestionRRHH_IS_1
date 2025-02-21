from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='rrhh/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', login_required(TemplateView.as_view(template_name="rrhh/dashboard.html")), name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('gestion-empleados/', views.empleados, name='empleados'),
    path('nominas/', views.nominas, name='nominas'),
    path('prestaciones/', views.prestaciones, name='prestaciones'),
    path('reportes/', views.reportes, name='reportes'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/nuevo/', views.nuevo_empleado, name='nuevo_empleado'),
    path('empleados/editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
]
