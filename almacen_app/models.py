from django.db import models
from datetime import date
from django.conf import settings
# Create your models here.

class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    estantes = models.ManyToManyField('Estante', blank=True)
    productos = models.ManyToManyField('Producto', blank=True)
    
    def __str__(self):
        return self.nombre

class Estante(models.Model):
    nombre = models.CharField(max_length=50)
    productos = models.ManyToManyField('Producto', blank=True)
    
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    codigo_barras = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(null=True, blank=True)
    oem = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.TextField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField(blank=True, null=True)
    compatibilidad = models.CharField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    campo_predefinido = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        choices = (
            ('Neumáticos y productos relacionados', 'Neumáticos y productos relacionados'),
            ('Aceites y líquidos', 'Aceites y líquidos'),
            ('Frenos', 'Frenos'),
            ('Filtros', 'Filtros'),
            ('Motor', 'Motor'),
            ('Sistema limpiaparabrisas', 'Sistema limpiaparabrisas'),
            ('Encendido y precalentamiento', 'Encendido y precalentamiento'),
            ('Suspensión', 'Suspensión'),
            ('Sistema eléctrico', 'Sistema eléctrico'),
            ('Amortiguación', 'Amortiguación'),
            ('Correas, cadenas, rodillos', 'Correas, cadenas, rodillos'),
            ('Sistema de refrigeración del motor', 'Sistema de refrigeración del motor'),
            ('Carrocería', 'Carrocería'),
            ('Calefacción y ventilación', 'Calefacción y ventilación'),
            ('Juntas y retenes', 'Juntas y retenes'),
            ('Escape', 'Escape'),
            ('Interior', 'Interior'),
            ('Sistema de combustible', 'Sistema de combustible'),
            ('Dirección', 'Dirección'),
            ('Embrague', 'Embrague'),
            ('Palier y junta homocinética', 'Palier y junta homocinética'),
            ('Remolque / piezas adicionales', 'Remolque / piezas adicionales'),
            ('Caja de cambios', 'Caja de cambios'),
            ('Aire acondicionado', 'Aire acondicionado'),
            ('Rodamientos', 'Rodamientos'),
            ('Árboles de transmisión y diferenciales', 'Árboles de transmisión y diferenciales'),
            ('Sensores, relés, unidades de control', 'Sensores, relés, unidades de control'),
            ('Accesorios para coches', 'Accesorios para coches'),
            ('Kits de reparación Y Herramientas', 'Kits de reparación Y Herramientas'),
            ('Tuberías y mangueras', 'Tuberías y mangueras'),
            ('Iluminación', 'Iluminación'),
            ('Sujeciones', 'Sujeciones'),
        )
    )

    def __str__(self):
        return self.codigo

class Bulto(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(default=date.today)
    insertado = models.BooleanField(default=False)
    productos = models.JSONField(default=list)

    def __str__(self):
        return self.nombre

  
class Despacho(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(default=date.today)
    productos = models.JSONField(default=list)
    cliente = models.CharField(max_length=50)
    insertado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class LoggerUsuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.usuario.username} - {self.action} - {self.timestamp}'
    
class Pedidos(models.Model):
   ESTADOS_PEDIDO = (
        ('realizado', 'Realizado'),
        ('espera', 'Espera'),
        ('aceptado', 'Aceptado'),
        ('cancelado', 'Cancelado'),
    ) 
   usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
   fecha_realizacion = models.DateTimeField(auto_now_add=True)
   detalles = models.TextField()  # Campo para almacenar los detalles del pedido como texto
   estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO)

   def __str__(self):
    return f'Pedido de {self.usuario.username} - {self.fecha_realizacion}'
    
