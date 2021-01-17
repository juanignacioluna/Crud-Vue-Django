from django.db import models

class tablaUNO(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
