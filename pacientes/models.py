from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

class Domicilio(models.Model):
    calle = models.CharField(max_length=200)
    altura = models.IntegerField()
    barrio = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    provincia =  models.CharField(max_length=200)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.altura} {self.barrio}'

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    apellido = models.CharField(max_length=50, verbose_name='apellido')
    dni = models.CharField(max_length=20)
    obrasocial = models.CharField(max_length=200) 
    numero_beneficiario = models.CharField(max_length=200) 
    email = models.EmailField(max_length=200)
    telefono = models.IntegerField()
    observaciones = models.TextField()          
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name='paciente'
            verbose_name_plural='pacientes'

    def __str__(self):
        return  f'Paciente: {self.id}: {self.nombre} {self.apellido}'
