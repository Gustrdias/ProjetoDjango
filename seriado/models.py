from django.db import models
from django.contrib.auth.models import User

class Seriado(models.Model):
    # lista genero
    LISTA_GENERO=(
        ('Ação','Ação'),
        ('Comédia','Comédia'),
        ('Drama','Drama'),
        ('Aventura','Aventura'),
        ('Terror','Terror'),
        ('Ciêntifico','Ciêntifico'),
        ('Romance','Romance'),
        ('Suspence','Suspence'),
        ('Musical','Musical')
    )
                   
    nome = models.CharField(max_length=100)
    genero= models.CharField(max_length=10, choices=LISTA_GENERO)
    avaliacao = models.IntegerField()
    assistido = models.CharField(max_length=10)
    imagemFile = models.FileField(upload_to='seriados',default='#')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    
