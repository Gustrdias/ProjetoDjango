from django.shortcuts import render, redirect
from django.core.management.base import BaseCommand, CommandError
from .models import Seriado
from .forms import SeriadoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def listarSeriados(request):
    current_user = request.user
    seriados = Seriado.objects.all().filter(user_id = current_user.id)
    return render(request, 'listar.html', {'seriados' : seriados})

@login_required
def criarSeriado(request):
    if request.method == 'POST':
        form = SeriadoForm(request.POST, request.FILES)
        #raise CommandError(form)
        if form.is_valid():
            form.save()
        return redirect('/seriados/')
    else:
        form = SeriadoForm()
        return render(request, 'editar.html', {'form' : form})

@login_required
def editarSeriado(request, id):
    seriado = Seriado.objects.get(pk=id)
    if request.method == 'POST':
        form = SeriadoForm(request.POST, request.FILES,instance=seriado)
        form.save()
        return redirect('/seriados/')
    else:
        form = SeriadoForm(instance=seriado)
        return render(request, 'editar.html',{'form' : form, 'seriado' : seriado})

@login_required
def deletarSeriado(request, id):
    seriado = Seriado.objects.get(pk=id)
    seriado.delete()
    return redirect('/seriados/')