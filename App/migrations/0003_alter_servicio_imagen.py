# Generated by Django 4.2.2 on 2024-04-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_servicio_tipo_delete_tiposervicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/servicios', verbose_name='Imagen del servicio'),
        ),
    ]