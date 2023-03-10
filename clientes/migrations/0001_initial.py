# Generated by Django 3.0.2 on 2022-12-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('DNI', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('fechainicio', models.DateField()),
            ],
        ),
    ]
