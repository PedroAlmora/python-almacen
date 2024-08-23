from almacen_app.models import Producto
from django.db.models import Count


def productos_cantidad_cero(request):
    productos_cantidad_cero = Producto.objects.filter(cantidad=0)
    return {'productos': productos_cantidad_cero}



def productos_cantidad_tipo(request):
    productos_cantidad_tipo = Producto.objects.values('campo_predefinido').annotate(cantidad_productos=Count('id')).order_by('campo_predefinido')
    
    colors = {
        'dot-primary': '#007bff',
        'dot-secondary': '#6c757d',
        'dot-success': '#28a745',
        'dot-danger': '#dc3545',
        'dot-warning': '#ffc107',
        'dot-info': '#17a2b8'
    }
    return {'producto_campo': productos_cantidad_tipo, 'colors': colors}