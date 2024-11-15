from django.db import models

# Create your models here.
class Pokemon(models.Model):
    """
    Modelo que representa la estructura de 
    datos de un pokemon en base de datos
    """
    nombre = models.CharField(max_length=200)
    peso = models.IntegerField()
    altura = models.FloatField()
    imagen = models.FileField(upload_to="pokemones/")

    def __str__(self):
        return self.nombre