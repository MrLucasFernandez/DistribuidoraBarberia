# Generated by Django 4.2.2 on 2024-05-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_categoria_producto_delete_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(verbose_name='Stock'),
        ),
    ]
