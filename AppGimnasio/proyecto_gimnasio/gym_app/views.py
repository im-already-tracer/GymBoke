from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from gym_app.forms import UsuarioForm
from gym_app.models import Usuario

from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario
from django.http import JsonResponse


# Create your views here.


def bienvenido(request):


    if request.method == 'POST':
        formaPersona = UsuarioForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        # formulario
        formaUsuario = UsuarioForm()
    return render(request, 'bienvenido.html', {'formaUsuario': formaUsuario})


def nuevoUsuario(request):
    if request.method == 'POST':
        formaUsuario = UsuarioForm(request.POST)

        if formaUsuario.is_valid():
            usuario = formaUsuario.save(commit=False)
            usuario.asignar_fecha_vencimiento_cuota()  # Llama al método para asignar la fecha de vencimiento de la cuota
            usuario.save()
            return redirect('index')
    else:
        formaUsuario = UsuarioForm()

    return render(request, 'nuevo_usuario.html', {'formaUsuario': formaUsuario})


def search_result(request):
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        res = None
        usuarios = request.POST.get('usuarios')
        query_se = Usuario.objects.filter(nombre__icontains=usuarios)

        if len(query_se) > 0 and len(usuarios) > 0:
            data = []
            for pos in query_se:
                item = {
                    'DNI': pos.dni,
                    'nombre': pos.nombre,
                    'apellido': pos.apellido,
                    'Ultimo Ingreso': pos.ultimoIngreso,
                    'UltimoPago': pos.ultimoPago,
                    'Vence cuota': pos.venceCuota,
                }

                data.append(item)
            res = data
        else:
            res = 'Usuario no encontrado'

        return JsonResponse({'data': res})
    return JsonResponse({})
