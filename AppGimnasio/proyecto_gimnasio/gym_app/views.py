from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from gym_app.forms import UsuarioForm
from gym_app.models import Usuario

from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario


# Create your views here.


def bienvenido(request):

    return render(request, 'bienvenido.html')


def nuevoUsuario(request):
    if request.method == 'POST':
        formaUsuario = UsuarioForm(request.POST)

        if formaUsuario.is_valid():
            usuario = formaUsuario.save(commit=False)
            usuario.asignar_fecha_vencimiento_cuota()  # Llama al método para asignar la fecha de vencimiento de la cuota
            usuario.save()
            return redirect('registros')
    else:
        formaUsuario = UsuarioForm()

    return render(request, 'nuevo_usuario.html', {'formaUsuario': formaUsuario})


def detalle_usuarios(request):
    usuarios = Usuario.objects.all()

    return render(request, 'usuarios.html', {'usuarios': usuarios})
def eliminar_usuario(request, dni):
    usuario = get_object_or_404(Usuario, pk = dni)
    if usuario:
        usuario.delete()
    return redirect('registros')
