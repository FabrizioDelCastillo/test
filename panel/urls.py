from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django import views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index, name="index"),
    path('listar', views.listar, name="listar"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar/<int:idUsuario>', views.actualizar, name="actualizar"),
    path('eliminar/<int:idUsuario>', views.eliminar, name="eliminar"),
    path('listar_ventas', views.listar_ventas, name="listar_ventas"),
    path('agregar_ventas', views.agregar_ventas, name="agregar_ventas"),
    path('actualizar_ventas/<int:idVenta>', views.actualizar_ventas, name="actualizar_ventas"),
    path('eliminar_ventas/<int:idVenta>', views.eliminar_ventas, name="eliminar_ventas"),
    path('listar_anuncios', views.listar_anuncios, name="listar_anuncios"),
    path('agregar_anuncios', views.agregar_anuncios, name="agregar_anuncios"),
    path('actualizar_anuncios/<int:idAnuncios>', views.actualizar_anuncios, name="actualizar_anuncios"),
    path('eliminar_anuncios/<int:idAnuncios>', views.eliminar_anuncios, name="eliminar_anuncios"),
    path('listar_asistencia', views.listar_asistencia, name="listar_asistencia"),
    path('agregar_asistencia', views.agregar_asistencia, name="agregar_asistencia"),
    path('actualizar_asistencia/<int:idAsistencia>', views.actualizar_asistencia, name="actualizar_asistencia"),
    path('eliminar_asistencia/<int:idAsistencia>', views.eliminar_asistencia, name="eliminar_asistencia"),
    path('listar_campana', views.listar_campana, name="listar_campana"),
    path('agregar_campana', views.agregar_campana, name="agregar_campana"),
    path('actualizar_campana/<int:idCampana>', views.actualizar_campana, name="actualizar_campana"),
    path('eliminar_campana/<int:idCampana>', views.eliminar_campana, name="eliminar_campana"),
    path('listar_cartera', views.listar_cartera, name="listar_cartera"),
    path('agregar_cartera', views.agregar_cartera, name="agregar_cartera"),
    path('actualizar_cartera/<int:idCartera>', views.actualizar_cartera, name="actualizar_cartera"),
    path('eliminar_cartera/<int:idCartera>', views.eliminar_cartera, name="eliminar_cartera"),
    path('listar_direccion', views.listar_direccion, name="listar_direccion"),
    path('agregar_direccion', views.agregar_direccion, name="agregar_direccion"),
    path('actualizar_direccion/<int:idDireccion>', views.actualizar_direccion, name="actualizar_direccion"),
    path('eliminar_direccion/<int:idDireccion>', views.eliminar_direccion, name="eliminar_direccion"),
    path('listar_estado', views.listar_estado, name="listar_estado"),
    path('agregar_estado', views.agregar_estado, name="agregar_estado"),
    path('actualizar_estado/<int:idEstado>', views.actualizar_estado, name="actualizar_estado"),
    path('eliminar_estado/<int:idEstado>', views.eliminar_estado, name="eliminar_estado"),
    path('listar_modalidad', views.listar_modalidad, name="listar_modalidad"),
    path('agregar_modalidad', views.agregar_modalidad, name="agregar_modalidad"),
    path('actualizar_modalidad/<int:idModalidad>', views.actualizar_modalidad, name="actualizar_modalidad"),
    path('eliminar_modalidad/<int:idModalidad>', views.eliminar_modalidad, name="eliminar_modalidad"),
    path('listar_observacion', views.listar_observacion, name="listar_observacion"),
    path('agregar_observacion', views.agregar_observacion, name="agregar_observacion"),
    path('actualizar_observacion/<int:idObservacion>', views.actualizar_observacion, name="actualizar_observacion"),
    path('eliminar_observacion/<int:idObservacion>', views.eliminar_observacion, name="eliminar_observacion"),
    path('listar_operador', views.listar_operador, name="listar_operador"),
    path('agregar_operador', views.agregar_operador, name="agregar_operador"),
    path('actualizar_operador/<int:idOperador>', views.actualizar_operador, name="actualizar_operador"),
    path('eliminar_operador/<int:idOperador>', views.eliminar_operador, name="eliminar_operador"),
    path('listar_paquete_movil', views.listar_paquete_movil, name="listar_paquete_movil"),
    path('agregar_paquete_movil', views.agregar_paquete_movil, name="agregar_paquete_movil"),
    path('actualizar_paquete_movil/<int:idPaquete_Movil>', views.actualizar_paquete_movil, name="actualizar_paquete_movil"),
    path('eliminar_paquete_movil/<int:idPaquete_Movil>', views.eliminar_paquete_movil, name="eliminar_paquete_movil"),
    path('listar_potencia', views.listar_potencia, name="listar_potencia"),
    path('agregar_potencia', views.agregar_potencia, name="agregar_potencia"),
    path('actualizar_potencia/<int:idPotencia>', views.actualizar_potencia, name="actualizar_potencia"),
    path('eliminar_potencia/<int:idPotencia>', views.eliminar_potencia, name="eliminar_potencia"),
    path('listar_segmento', views.listar_segmento, name="listar_segmento"),
    path('agregar_segmento', views.agregar_segmento, name="agregar_segmento"),
    path('actualizar_segmento/<int:idSegmento>', views.actualizar_segmento, name="actualizar_segmento"),
    path('eliminar_segmento/<int:idSegmento>', views.eliminar_segmento, name="eliminar_segmento"),
    path('listar_tarifa', views.listar_tarifa, name="listar_tarifa"),
    path('agregar_tarifa', views.agregar_tarifa, name="agregar_tarifa"),
    path('actualizar_tarifa/<int:idTarifa>', views.actualizar_tarifa, name="actualizar_tarifa"),
    path('eliminar_tarifa/<int:idTarifa>', views.eliminar_tarifa, name="eliminar_tarifa"),
    path('listar_tecnologia', views.listar_tecnologia, name="listar_tecnologia"),
    path('agregar_tecnologia', views.agregar_tecnologia, name="agregar_tecnologia"),
    path('actualizar_tecnologia/<int:idTecnologia>', views.actualizar_tecnologia, name="actualizar_tecnologia"),
    path('eliminar_tecnologia/<int:idTecnologia>', views.eliminar_tecnologia, name="eliminar_tecnologia"),

    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)