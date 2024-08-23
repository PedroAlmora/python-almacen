from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from users_app.models import Usuario
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import Permission
from .forms import LoginForm, CustomPasswordChangeForm, RegistroUsuarioForm
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from almacen_app.views import calcular_sumatoria_precios, calcular_cantidad_productos, calcular_total_productos_agotados, calcular_porcentaje_disponibilidad, obtener_datos_area


#######################################AUTENTICACIÓN###############################################

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            add_bootstrap_message(request, 'success', ' Bienvenido {}'.format(user.username))
            return redirect('/index')
        else:
            add_bootstrap_message(request, 'warning', ' Usuario o contraseña no validos')
       
    return render (request,  'login.html',{ })

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    add_bootstrap_message(request, 'success', 'Sesión cerrada exitosamente')
    login_url = reverse('login_app:login')
    return redirect(login_url)

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualizar la sesión con la contraseña cambiada
            add_bootstrap_message(request, 'success', '¡Contraseña cambiada exitosamente!')
            return redirect('login_app:index')  # Redirigir a la página de perfil o a la ruta que desees
        else:
           add_bootstrap_message(request, 'warning', 'Por favor. Verifique los campos')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'cambiar_contrasena.html', {'form': form})


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Guarda el formulario sin guardar en la base de datos
            user.set_password(form.cleaned_data['password1'])  # Establece la contraseña encriptada
            user.save()  # Ahora guarda el usuario en la base de datos

            # Agregar todos los permisos al usuario
            User = get_user_model()
            all_permissions = Permission.objects.all()
            user.user_permissions.set(all_permissions)
            add_bootstrap_message(request, 'success', '¡Almacén creado exitosamente!')
            return redirect(reverse('login_app:lista_usuarios'))
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})
###################################################################################################

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('login_app:lista_usuarios')
  

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Redirige a alguna página de éxito, como la lista de usuarios o el perfil del usuario actualizado.
            return redirect('login_app:lista_usuarios')
    else:
        form = RegistroUsuarioForm(instance=usuario)

    return render(request, 'registrar_usuario.html', {
        'form': form,
        'editar': True,  # Esta variable se utilizará para cambiar el título del h4 y el texto del botón.
    })

@login_required(login_url="login")
@csrf_protect
def index(request):
    sumatoria_precios = calcular_sumatoria_precios(request)
    cantidad_productos = calcular_cantidad_productos(request)
    total_agotados = calcular_total_productos_agotados(request)
    porcentaje_disponibilidad = calcular_porcentaje_disponibilidad(request)
    context = {'sumatoria_precios': sumatoria_precios,
               'cantidad_productos': cantidad_productos,
               'total_agotados': total_agotados,
               'porcentaje_disponibilidad': porcentaje_disponibilidad,
               }
    return render(request, 'index.html', context)    

def add_bootstrap_message(request, level, message):
    tags = {
        'success': 'alert-success',
        'info': 'alert-info',
        'warning': 'alert-warning',
        'error': 'alert-danger',
    }
    messages.add_message(request, getattr(messages, level.upper()), message, extra_tags='alert {}'.format(tags[level]))