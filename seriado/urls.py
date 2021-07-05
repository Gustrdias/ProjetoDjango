from django.shortcuts import render
from . import views
from django.urls import path

urlpatterns = [
    path('seriados/', views.listarSeriados, name='listar-seriados'),
    path('seriados/novo', views.criarSeriado, name='novo-seriado'),
    path('seriados/<int:id>', views.editarSeriado, name='editar-seriado'),
    path('seriados/delete/<int:id>', views.deletarSeriado, name='deletar-seriado')
]