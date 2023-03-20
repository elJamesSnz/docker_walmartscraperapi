from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    name = models.CharField(max_length=200)
    url = models.URLField()