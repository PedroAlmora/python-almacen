from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Crea un superusuario con roles'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--rol', dest='rol', default='admin', help='Rol del usuario')
        parser.add_argument('--contrasena', dest='contrasena', default=None, help='Contraseña del usuario')
        parser.add_argument('--correo', dest='correo', default=None, help='Correo electrónico del usuario')

    def handle(self, *args, **options):
        rol = options['rol']
        contrasena = options['contrasena']
        correo = options['correo']

        if not contrasena or not correo:
            raise CommandError("Debes proporcionar una contraseña y un correo electrónico.")

        options['rol'] = rol
        options['password'] = contrasena
        options['email'] = correo

        return super().handle(*args, **options)