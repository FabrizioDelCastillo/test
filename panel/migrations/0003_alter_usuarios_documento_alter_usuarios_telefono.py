# Generated by Django 4.2.1 on 2023-10-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_usuarios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='documento',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]