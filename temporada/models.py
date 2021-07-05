from django.db import models
from seriado.models import Seriado

class Temporada(models.Model):
    numero = models.IntegerField()
    seriado_id = models.ForeignKey(Seriado, on_delete=models.CASCADE)
    imagemFile = models.FileField(upload_to='temporadas',default='#')
