# Generated by Django 4.2.1 on 2023-11-07 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_alter_anuncios_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartera',
            old_name='correo',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='cartera',
            old_name='f_nac',
            new_name='f_final',
        ),
        migrations.RenameField(
            model_name='cartera',
            old_name='documento',
            new_name='operador',
        ),
        migrations.RenameField(
            model_name='cartera',
            old_name='telefono',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='cartera',
            old_name='apellido',
            new_name='tipo',
        ),
    ]