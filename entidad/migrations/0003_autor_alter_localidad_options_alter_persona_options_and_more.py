# Generated by Django 4.1.2 on 2022-10-19 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0002_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Autores',
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.AlterModelOptions(
            name='localidad',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Localidades'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['apellido', 'nombre']},
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('editorial', models.CharField(max_length=100)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entidad.autor')),
            ],
        ),
    ]