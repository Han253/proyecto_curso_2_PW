from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detalle/<id_pokemon>/',views.vista_detalle, name='detallePokemon'),
]