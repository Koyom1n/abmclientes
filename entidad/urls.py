from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('acerca-de', views.acerca_de, name="acerca-de"),
    path('clientes', views.clientes, name="clientes"),
    #path('clientes/<str:nombre_cliente>', views.cliente, name="cliente"),
    path('nuevo_cliente', views.nuevo_cliente, name="nuevo_cliente"),
    path('cliente/<int:pk>', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:pk>', views.eliminar_cliente, name='eliminar_cliente'),
    path('localidades', views.localidades, name="localidades"),
    path('nueva_localidad', views.nueva_localidad, name='nueva_localidad'),
    path('localidad/<int:pk>', views.eliminar_localidad, name='eliminar_localidad'),
    path('localidad/<int:pk>', views.modificar_localidad, name="modificar_localidad"),
]