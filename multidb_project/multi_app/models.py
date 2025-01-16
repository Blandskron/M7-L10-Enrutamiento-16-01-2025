from django.db import models

class ModeloPrimario(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'multi_app'
        db_table = 'modelo_primario'

class ModeloSecundario(models.Model):
    apellido = models.CharField(max_length=100)

    class Meta:
        app_label = 'multi_app'
        db_table = 'secondary'
        