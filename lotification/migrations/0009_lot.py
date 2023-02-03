# Generated by Django 4.1.5 on 2023-01-28 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotification', '0008_delete_lotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitud', models.FloatField(null=True)),
                ('ancho', models.FloatField(null=True)),
                ('precio', models.FloatField(null=True)),
                ('estado', models.CharField(choices=[('Ocupado', 'Ocupado'), ('Disponible', 'Disponible')], max_length=25, null=True)),
                ('vendedor', models.CharField(blank=True, max_length=25, null=True)),
                ('comprador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lotification.clients')),
            ],
        ),
    ]