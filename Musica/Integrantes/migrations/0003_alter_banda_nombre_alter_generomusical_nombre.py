# Generated by Django 5.0.6 on 2024-05-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Integrantes', '0002_remove_banda_generos_remove_banda_integrantes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='generomusical',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
