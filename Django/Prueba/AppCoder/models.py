from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=50)
    #foto = models.ImageField(upload_to='fotos', null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido