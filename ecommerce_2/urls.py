from django.contrib import admin
from django.urls import path
from ecommerce_2.views import (inicio, 
    mostrar_productos, mostrar_vencimientos, mostrar_index)

ecommerce_patterns = ([
    path('inicio/', inicio, name='inicio'),
    path('mi-pagina/', mostrar_index, name= 'index'),
    path('productos/', mostrar_productos, name='productos'),
    path('vencimientos/', mostrar_vencimientos, name='vencimientos'),
],'ecommerce')