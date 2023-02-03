# Generated by Django 4.1.5 on 2023-01-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotification', '0003_time_struct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_struct',
            name='date_lastupdated',
        ),
        migrations.AddField(
            model_name='time_struct',
            name='lastupdated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='time_struct',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]