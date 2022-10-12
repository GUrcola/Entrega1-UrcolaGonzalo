from random import Random, random
from re import template
from django.http import HttpResponse
from datetime import date, datetime
from django.template import Context, Template, loader
from Familia.models import familiares

def crear_familiar (request,nombre,apellido,edad):
    familia= familiares(nombre=nombre,apellido=apellido,edad=edad)
    familiares.save(nombre,apellido,edad)


    cargar_archivo= open(r'C:\Users\Tango\Desktop\Familia-Proyecto\Templates\crear_familiar.html','r')
    template= Template(cargar_archivo.read())
    cargar_archivo.close()
    template_renderizado= template.render()
    return HttpResponse (template_renderizado)  



def ver_familia (request):
   
   familia=familiares.objects.all()
   template= loader.get_template('ver_familia.html')
   template_renderizado=template.render({'familia': familia})
      
   return HttpResponse(template_renderizado)    


