# Generated by Django 4.2.6 on 2023-10-15 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('insertado', models.BooleanField(default=False)),
                ('productos', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('productos', models.JSONField(default=list)),
                ('cliente', models.CharField(max_length=50)),
                ('insertado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('codigo_barras', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('compatibilidad', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('campo_predefinido', models.CharField(blank=True, choices=[('motor', 'Motor'), ('transmisión', 'Transmisión'), ('suspensión', 'Suspensión'), ('frenos', 'Frenos'), ('carrocería', 'Carrocería'), ('eléctrica', 'Eléctrica'), ('neumáticos', 'Neumáticos'), ('accesorios', 'Accesorios')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('productos', models.ManyToManyField(blank=True, to='almacen_app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estantes', models.ManyToManyField(blank=True, to='almacen_app.estante')),
                ('productos', models.ManyToManyField(blank=True, to='almacen_app.producto')),
            ],
        ),
    ]
