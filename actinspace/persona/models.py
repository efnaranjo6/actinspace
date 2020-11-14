from django.db import models
# Create your models here.
class Persona(models.Model):
    nombrePersona = models.CharField(max_length=200)
    apellidoPersona = models.CharField(max_length=200)
    codgps = models.CharField(max_length=300)


    def __str__(self):
        return '{}'.format(self.nombrePersona)
    def save(self):
        self.nombrePersona = self.nombrePersona
        self.apellidoPersona = self.apellidoPersona
        self.codgps = self.codgps


class Meta:
    verbose_name_plural = 'Personas'
