# Generated by Django 4.2.1 on 2023-10-31 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_rename_correo_anuncios_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncios',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
