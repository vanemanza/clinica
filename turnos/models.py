from django.db import models
from pacientes.models import Pacientes
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

class Turnos(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="turnos_secretaria")
    medico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="turnos_medico")
    fecha = models.DateTimeField(auto_now_add=True)
    asistencia = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name='turno'
            verbose_name_plural='turnos'

    def __str__(self):
        return  f'{self.fecha}: {self.paciente} {self.medico}'


