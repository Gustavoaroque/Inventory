# Generated by Django 4.1.5 on 2023-01-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotification', '0004_remove_time_struct_date_lastupdated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.BigIntegerField(null=True)),
                ('direccion', models.TextField(null=True)),
            ],
        ),
    ]