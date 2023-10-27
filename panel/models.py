from django.db import models

# Create your models here.


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'usuarios' 
        
class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'ventas' 