from django.shortcuts import render, redirect
from django.core.management.base import BaseCommand, CommandError
from .models import Temporada
from seriado.models import Seriado
from .forms import TemporadaForm
from django.contrib.auth.decorators import login_required

@login_required
def listarTemporadas(request, seriado_id):
    temporada = Temporada.objects.filter(seriado_id = seriado_id)
    #raise CommandError(temporada)
    seriado = Seriado.objects.get(pk=seriado_id)
    return render(request, 'listarTemp.html', {'temporadas' : temporada, 'seriado' : seriado})

@login_required
def criarTemporada(request,seriado_id):
    if request.method == 'POST':
        form = TemporadaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/seriados/"+str(seriado_id)+"/temporadas")
    else:
        form = TemporadaForm()
        return render(request, 'editarTemp.html', {'form' : form , "seriado_id" : seriado_id})

@login_required
def editarTemporada(request,id ,seriado_id):
    temporada = Temporada.objects.get(pk=id)
    if request.method == 'POST':
        form = TemporadaForm(request.POST, request.FILES, instance=temporada)
        if form.is_valid():
            form.save()
            return redirect("/seriados/"+str(seriado_id)+"/temporadas")
    else:
        form = TemporadaForm(instance=temporada)
        return render(request, 'editarTemp.html',{'form' : form, 'temporada' : temporada,"seriado_id" : seriado_id})

@login_required
def deletarTemporada(request, id,seriado_id):
    temporada = Temporada.objects.get(pk=id)
    temporada.delete()
    return redirect("/seriados/"+str(seriado_id)+"/temporadas")