# Generated by Django 4.2.1 on 2023-11-07 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_rename_correo_cartera_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direccion',
            old_name='apellido',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='f_nac',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='telefono',
        ),
    ]