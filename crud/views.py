from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#Importar Modelo
from .models import Pokemon

# Create your views here.
def index(request):
    #Consultar listado de registros de base de datos
    lista_pokemones = Pokemon.objects.all()    
    template = loader.get_template("index.html")
    #Agregar pokemones al contexto del template
    context = {"pokemones":lista_pokemones}
    return HttpResponse(template.render(context,request))

def vista_detalle(request, id_pokemon):
    #Consultar el registro en base de datos
    detalle_pokemon = Pokemon.objects.get(id = id_pokemon)
    #Obtener template
    template = loader.get_template("detail.html")
    #Agregar los datos del registro al contexto del template
    context = {"pokemon":detalle_pokemon}
    return HttpResponse(template.render(context,request))