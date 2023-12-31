# Generated by Django 4.2.1 on 2023-10-28 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_ventas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'anuncios',
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'asistencia',
            },
        ),
        migrations.CreateModel(
            name='Campana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'campana',
            },
        ),
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'cartera',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'direcion',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'modalidad',
            },
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'observacion',
            },
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'operador',
            },
        ),
        migrations.CreateModel(
            name='Paquete_Movil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'paquete_movil',
            },
        ),
        migrations.CreateModel(
            name='Potencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'potencia',
            },
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'segmento',
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'tarifa',
            },
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('f_nac', models.DateField()),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'tecnologia',
            },
        ),
    ]
