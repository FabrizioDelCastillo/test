# Generated by Django 4.2.1 on 2023-10-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
