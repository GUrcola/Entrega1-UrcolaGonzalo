from re import template
from django.http import HttpResponse
from django.template import Context, Template, loader
from Familia.models import familiares
from django.shortcuts import render

def crear_familiar (request,nombre,apellido,edad):
    familia= familiares(nombre=nombre,apellido=apellido,edad=edad)
    familia.save(nombre,apellido,edad)


    # template= loader.get_template('crear_familiar.html')
    # template_renderizado= template.render()
    # return HttpResponse (template_renderizado)  
    return render(request, 'Familia/crear_familiar.html', {'familia': familia})



def ver_familia (request):
   
   familia=familiares.objects.all()
   template= loader.get_template('ver_familia.html')
   template_renderizado=template.render({'familia': familia})
      
   return HttpResponse(template_renderizado)    


