from django.db import models

class Data(models.Model):
    try:
        id = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        edad = models.CharField(max_length=100)
        nota = models.CharField(max_length=10)
    except Exception as e:
        print('Modelo no creado: ', e)