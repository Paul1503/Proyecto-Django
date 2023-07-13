# Generated by Django 4.2.2 on 2023-07-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_boleta_alter_categoria_idcategoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('procesandoPedido', 'Procesando Pedido'), ('enviado', 'Enviado'), ('enCamino', 'En camino'), ('entregado', 'Entregado')], default='procesandoPedido', max_length=25),
        ),
    ]
