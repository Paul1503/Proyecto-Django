# Generated by Django 4.2.2 on 2023-07-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_alter_producto_descripcion_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=35, verbose_name='Descripcion'),
        ),
    ]
