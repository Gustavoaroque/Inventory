# Generated by Django 4.1.5 on 2023-01-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotification', '0002_alter_lote_comprador_alter_lote_vendedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='time_struct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('added', models.DateField(auto_now_add=True)),
                ('date_lastupdated', models.DateField(auto_now=True)),
            ],
        ),
    ]