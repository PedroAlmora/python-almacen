from .models import LoggerUsuario

def registrarLoggerUsuario(user, action):
    LoggerUsuario.objects.create(usuario=user, action=action)

def obtenerActividadesLogger():
    actividades = LoggerUsuario.objects.all()
    datos_actividades = []

    for actividad in actividades:
        datos_actividad = {
            'id': actividad.id,
            'username': actividad.usuario.username,
            'action': actividad.action,
            'fecha': actividad.timestamp,
        }
        datos_actividades.append(datos_actividad)

    return datos_actividades