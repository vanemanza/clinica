# Generated by Django 2.2.4 on 2021-08-09 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_auto_20210808_2005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]