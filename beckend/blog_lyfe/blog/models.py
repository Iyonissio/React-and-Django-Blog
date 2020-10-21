from django.db import models
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


class Categorias(models.TextChoices):
    MUNDO = 'MUN','Mundo'
    AMBIENTE = 'AMB','Ambiente'
    TECNOLOGIA = 'TEC','Tecnologia'
    DESIGN = 'DES','Design'
    CULTURA = 'CUL','Cultura'
    NEGOCIO = 'NEG','Negocio'
    POLITICA = 'POL','Politica'
    OPINIAO = 'OPI','Opiniao'
    CIENCIA = 'CIE','Ciencia'
    SAUDE = 'SAU','Saude'
    ESTILO = 'EST','Estilo'
    VIAGENS = 'VIA','Viagens'

class BlogPost(models.Model):
    titulo = models.CharField(max_length=400)
    slug = models.SlugField()
    categorias = models.CharField(max_length=50 , choices=Categorias.choices,default=Categorias.MUNDO)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    resumo = models.CharField(max_length=60)
    mes = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    conteudo = models.TextField(max_length=500)
    destaque = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

