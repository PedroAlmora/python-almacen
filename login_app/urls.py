from django.urls import path, include
from . import views_login
from django.conf import settings
from django.conf.urls.static import static
from almacen_app.urls import urlpatterns as  almacen_urls
from almacen_app.views import *



app_name = 'login_app'

urlpatterns = [
    path('', views_login.login_view, name='login'),
    path('index', views_login.index, name='index'),
    path('logout',views_login.logout_view, name="logout"),
    path('cambiar_contrasenna', views_login.cambiar_contrasena, name='cambiar_contrasenna'),
    path('registrar_usuario/', views_login.registrar_usuario, name='registrar_usuario'),
    path('lista_usuarios/', views_login.lista_usuarios, name='lista_usuarios'),
    path('eliminar_usuario/<int:usuario_id>/', views_login.eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:usuario_id>/', views_login.editar_usuario, name='editar_usuario'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
