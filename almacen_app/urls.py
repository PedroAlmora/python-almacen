from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from login_app import views_login
from .views import *



app_name = 'almacen_app'

urlpatterns = [
    path('', include('login_app.urls')),
    path('logsUsers', views.LoggerUser, name='logsUsers'),
    path('delete_logger/<int:logger_id>/', views.delete_logger, name='delete_logger'),
    path('productos_agotados', views.agotados, name='productos_agotados'),
    ########################ACCESO-TABLAS#################################
    path('productos', views.Productos, name='productos'),
    path('neumaticos/', views.neumaticos, name='neumaticos'),
    path('frenos/', views.frenos, name='frenos'),
    path('filtros/', views.filtros, name='filtros'),
    path('motor/', views.motor, name='motor'),
    path('aceites-y-lubricantes/', views.aceites_y_lubricantes, name='aceites_y_lubricantes'),
    path('limpiaparabrisas-y-escobillas/', views.limpiaparabrisas_y_escobillas, name='limpiaparabrisas_escobillas'),
    path('suspension/', views.suspension, name='suspension'),
    path('sistema-electrico/', views.sistema_electrico, name='sistema_electrico'),
    path('endendido-y-precalentamiento/', views.endendido_y_precalentamiento, name='endendido_precalentamiento'),
    path('correas-cadenas-rodillos/', views.correas_cadenas_rodillos, name='correas_cadenas_rodillos'),
    path('carroceria/', views.carroceria, name='carroceria'),
    path('calefaccion-y-ventilacion/', views.calefaccion_y_ventilacion, name='calefaccion_ventilacion'),
    path('baterias/', views.baterias, name='baterias'),
    path('sistema-de-combustible/', views.sistema_de_combustible, name='sistema_combustible'),
    path('direccion/', views.direccion, name='direccion'),
    path('amortiguacion/', views.amortiguacion, name='amortiguacion'),
    path('sistema-de-refrigeracion/', views.sistema_de_refrigeracion, name='sistema_refrigeracion'),
    path('juntas-y-retrenes/', views.juntas_y_retrenes, name='juntas_retrenes'),
    path('interior/', views.interior, name='interior'),
    path('embrague/', views.embrague, name='embrague'),
    path('caja-de-cambios/', views.caja_de_cambios, name='caja_cambios'),
    path('aire-acondicionado/', views.aire_acondicionado, name='aire_acondicionado'),
    path('rodamientos/', views.rodamientos, name='rodamientos'),
    path('transmision-diferencial/', views.transmision_y_diferencial, name='transmision_diferencial'),
    path('kit-de-reparacion/', views.kit_de_reparacion, name='kit_reparacion'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('tuberias-y-mangueras/', views.tuberias_y_mangueras, name='tuberias_mangueras'),
    path('iluminacion/', views.iluminacion, name='iluminacion'),
    path('sujeciones/', views.sujeciones, name='sujeciones'),
    path('sensores-relés-unidades-de-control/', views.sensores_reles, name='sensores-relés-unidades-de-control'),
    path('remolque-piezas-adicionales/', views.remolque_piezas_adicionales, name='remolque-piezas-adicionales'),
    path('pailer-juntas-homocinetica/', views.pailer_juntas_homocinetica, name='pailer-juntas-homocinetica'),
    #######################################################################
    path('create_producto', views.create_product, name='create_producto'),
    path('edit_producto/<int:product_id>/', views.edit_product, name='edit_producto'),
    path('delete_producto/<int:product_id>/', views.delete_product, name='delete_producto'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
    path('buscar-producto-general/<str:busqueda>', views.buscar_producto_por_codigo_de_barras, name='buscar-producto-general'),
    path('detalle_producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    #########################################################################################
    path('bultos/', views.mostrar_bultos, name='bultos'),
    path('create_bulto/', views.escanear_codigo_barras, name='create_bulto'),
    path('create_bulto_final/', views.crear_bulto, name='create_bulto_final'),
    path('delete_bulto/<int:bulto_id>/', views.delete_bulto, name='delete_bulto'),
    path('detalles_bulto/<int:bulto_id>/', views.detalles_bulto, name='detalles_bulto'),
    path('insertar_bulto/<int:bulto_id>/', views.actualizar_cantidad_productos, name='insertar_bulto'),
    #######################################################################################
    path('almacenes/', views.listar_almacenes, name='almacenes'),
    path('create_almacen', views.crear_almacen, name='create_almacen'),
    path('edit_almacen/<int:almacen_id>/', views.editar_almacen, name='edit_almacen'),
    path('delete_almacen/<int:almacen_id>/', views.eliminar_almacen, name='delete_almacen'),
    path('detalles_almacen/<int:almacen_id>/', views.detalle_almacen, name='detalle_almacen'),
    path('add_almacen/<int:producto_id>/', views.get_agregar_producto_a_almacenes, name='add_almacen'),
    path('post_add_almacen/<int:producto_id>/', views.agregar_producto_a_almacenes, name='post_add_almacen'),
    #######################################################################################
    path('estantes/', views.listar_estantes, name='estantes'),
    path('create_estante', views.crear_estante, name='create_estante'),
    path('edit_estante/<int:estante_id>/', views.editar_estante, name='edit_estante'),
    path('delete_estante/<int:estante_id>/', views.eliminar_estante, name='delete_estante'),
    path('detalles_estante/<int:estante_id>/', views.detalle_estante, name='detalles_estante'),
    path('add_estante/<int:producto_id>/', views.get_agregar_producto_a_estantes, name='add_estante'),
    path('post_add_estante/<int:producto_id>/', views.agregar_producto_a_estantes, name='post_add_estante'),
    #########################################################################################
    path('despachos/', views.mostrar_despachos, name='despachos'),
    path('create_despacho/', views.escanear_codigo_barras_despacho, name='create_despacho'),
    path('create_despacho_final/', views.crear_despacho, name='create_despacho_final'),
    path('delete_despacho/<int:despacho_id>/', views.delete_despacho, name='delete_despacho'),
    path('detalles_despacho/<int:despacho_id>/', views.detalles_despacho, name='detalles_despacho'),
    path('insertar_despacho/<int:despacho_id>/', views.decrementar_cantidad_productos, name='insertar_despacho'),
    path('exportar_despacho/<int:despacho_id>/', views.exportar_despacho_excel, name='exportar_despacho'),
    path('cargar_despacho_excel/', views.mostrar_excel_despacho, name='cargar_despacho_excel'),

    #############################################################################################################
    path('exportar_excel/', views.export_excel, name='exportar_excel'),
    path('importar_excel/', views.cargar_productos_excel, name='importar_excel'),
    path('exportar_excel_productos/', views.descargar_excel_productos, name='exportar_excel_productos'),
    path('exportar_excel_despacho/', views.descargar_excel_despacho, name='exportar_excel_despacho'),
    
    path('search_productos/<str:valor>', views.filtrar_productos_por_valor, name='search_productos'),
]    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

