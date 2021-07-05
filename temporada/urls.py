from django.shortcuts import render
from . import views
from django.urls import path

urlpatterns = [
    path('seriados/<int:seriado_id>/temporadas', views.listarTemporadas, name='listar-temporadas'),
    path('seriados/<int:seriado_id>/temporadas/novo', views.criarTemporada, name='nova-temporada'),
    path('seriados/<int:seriado_id>/temporadas/<int:id>', views.editarTemporada, name='editar-temporada'),
    path('seriados/<int:seriado_id>/temporadas/delete/<int:id>', views.deletarTemporada, name='deletar-temporada')
]