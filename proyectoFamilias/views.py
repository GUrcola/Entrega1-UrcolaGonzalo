from random import Random, random
from re import template
from django.http import HttpResponse
from datetime import date, datetime
from django.template import context, Template, loader
from Familia.models import familiares

def crear_familiar (request):
    familiares(nombre='Virginia',apellido='Urcola',edad=24,fecha_nacimiento=datetime(1997,8,2)),
    familiares(nombre='Horacio',apellido='Urcola',edad=57,fecha_nacimiento=datetime(1964,12,24)),
    familiares(nombre='Justo',apellido='Urcola',edad=16,fecha_nacimiento=datetime(2006,2,28)),
    familiares(nombre='Monica',apellido='Papagni',edad=50,fecha_nacimiento=datetime(1972,10,22))
    familiares.save()

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


