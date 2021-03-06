# Generated by Django 2.2.4 on 2021-08-07 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos', models.CharField(choices=[('lentes', 'lentes'), ('armazones', 'armazones'), ('ortóptica', 'ortóptica'), ('accesorios', 'accesorios')], max_length=20, verbose_name='categorias')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pedidos')),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField(default=1, null=True)),
                ('categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.Categoria')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('forma_pago', models.CharField(choices=[('tarjeta', 'tarjeta'), ('efectivo', 'efectivo'), ('debito', 'debito')], default='tarjeta', max_length=20, verbose_name='Forma de pago')),
                ('estado', models.CharField(choices=[('pendiente', 'pendiente'), ('pedido', 'pedido'), ('taller', 'taller'), ('finalizado', 'finalizado')], default='pendiente', max_length=1, verbose_name='Estado')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Pacientes')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Productos')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
    ]
