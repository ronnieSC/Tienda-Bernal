# Generated by Django 3.0.2 on 2022-12-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0004_auto_20221226_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='CatImg',
            field=models.ImageField(null=True, upload_to='pics/categorias', verbose_name='Imagen'),
        ),
    ]
