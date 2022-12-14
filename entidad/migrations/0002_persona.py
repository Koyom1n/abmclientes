# Generated by Django 4.1.2 on 2022-10-14 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_nac', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('tipo_iva', models.CharField(choices=[('CF', 'Consumidor final'), ('RI', 'Responsable inscripto'), ('MT', 'Monotributista')], default='CF', max_length=2, verbose_name='Tipo de IVA')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='entidad.localidad')),
            ],
        ),
    ]
