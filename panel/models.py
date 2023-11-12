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

class Anuncios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    f_final = models.DateField()
    imagen = models.ImageField(
        upload_to="media", null=True, blank=True)   
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'anuncios' 

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'asistencia'

class Campana(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    pais = models.CharField(max_length=20, null=False)
    operador = models.CharField(max_length=20, null=False)
    f_final = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'campana'

class Cartera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    pais = models.CharField(max_length=20, null=False)
    operador = models.CharField(max_length=20, null=False)
    f_final = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta: 
        db_table = 'cartera'
        

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'direcion'


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'estado'


class Modalidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'modalidad'


class Observacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'observacion'

class Operador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'operador'

class Paquete_Movil(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'paquete_movil'


class Potencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'potencia'

class Segmento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'segmento'


class Tarifa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'tarifa'


class Tecnologia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=20, null=False)
    f_nac = models.DateField()
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = 'tecnologia'