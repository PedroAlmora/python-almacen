# Generated by Django 4.2.4 on 2024-04-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen_app', '0010_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='campo_predefinido',
            field=models.CharField(blank=True, choices=[('Neumáticos y productos relacionados', 'Neumáticos y productos relacionados'), ('Aceites y líquidos', 'Aceites y líquidos'), ('Frenos', 'Frenos'), ('Filtros', 'Filtros'), ('Motor', 'Motor'), ('Sistema limpiaparabrisas', 'Sistema limpiaparabrisas'), ('Encendido y precalentamiento', 'Encendido y precalentamiento'), ('Suspensión', 'Suspensión'), ('Sistema eléctrico', 'Sistema eléctrico'), ('Amortiguación', 'Amortiguación'), ('Correas, cadenas, rodillos', 'Correas, cadenas, rodillos'), ('Sistema de refrigeración del motor', 'Sistema de refrigeración del motor'), ('Carrocería', 'Carrocería'), ('Calefacción y ventilación', 'Calefacción y ventilación'), ('Juntas y retenes', 'Juntas y retenes'), ('Escape', 'Escape'), ('Interior', 'Interior'), ('Sistema de combustible', 'Sistema de combustible'), ('Dirección', 'Dirección'), ('Embrague', 'Embrague'), ('Palier y junta homocinética', 'Palier y junta homocinética'), ('Remolque / piezas adicionales', 'Remolque / piezas adicionales'), ('Caja de cambios', 'Caja de cambios'), ('Aire acondicionado', 'Aire acondicionado'), ('Rodamientos', 'Rodamientos'), ('Árboles de transmisión y diferenciales', 'Árboles de transmisión y diferenciales'), ('Sensores, relés, unidades de control', 'Sensores, relés, unidades de control'), ('Accesorios para coches', 'Accesorios para coches'), ('Kits de reparación y herramientas', 'Kits de reparación y herramientas'), ('Tuberías y mangueras', 'Tuberías y mangueras'), ('Iluminación', 'Iluminación'), ('Sujeciones', 'Sujeciones')], max_length=50, null=True),
        ),
    ]
