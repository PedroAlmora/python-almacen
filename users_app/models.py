from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('visitante', 'Visitante'),
        ('almacenero', 'Almacenero'),
        ('economico', 'Económico'),
        ('rrhh', 'Recursos Humanos'),
    )

    rol = models.CharField(max_length=100, choices=ROL_CHOICES, null=True, blank=True)
    tarjeta_credito = models.CharField(max_length=100, null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='usuarios')

    def __str__(self):
        return self.username