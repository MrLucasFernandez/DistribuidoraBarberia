# Generated by Django 4.2.2 on 2024-05-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_servicio_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]
