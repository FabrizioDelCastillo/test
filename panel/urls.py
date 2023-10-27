from django.contrib import admin
from django.urls import path

from django import views
from . import views

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
] 
