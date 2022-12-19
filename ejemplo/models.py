from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}"

class Hijos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}"

class Padres(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}"