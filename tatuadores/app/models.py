from django.db import models

# Create your models here.
class tatuadores(models.Model):
    nombre=models.CharField(max_length=50)
    experiencia=models.CharField(max_length=50)
    estilo=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=9)
