from django.db import models

from garagem.models import Categoria, Marca

class Modelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelo")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelo")
    
    def __str__(self):
        return f"{self.nome} "

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
