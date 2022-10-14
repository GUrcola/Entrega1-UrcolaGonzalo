from contextlib import redirect_stderr
from re import template
from django.http import HttpResponse
from django.template import Context, Template
# loader
from Familia.models import familiares
from django.shortcuts import render, redirect

def crear_familiar (request):
    if request.method =='POST':
        nombre= request.POST.get('nombre')
        apellido= request.POST.get('apellido')
        familia= familiares(nombre=nombre,apellido=apellido)
        familia.save()
        return redirect('ver familia')    
        
    # template= loader.get_template('crear_familiar.html')
    # template_renderizado= template.render()
    # return HttpResponse (template_renderizado)  
    return render(request,'Familia/crear_familiar.html',{})



def ver_familia (request):
   
   familia=familiares.objects.all()
   return render(request,'Familia/ver_familia.html',{'familia': familia}) 
#    template= loader.get_template('ver_familia.html')
#    template_renderizado=template.render({'familia': familia})
      
#    return HttpResponse(template_renderizado) 
      
def index (request):
    return render(request, 'Familia/index.html')

def About (request):
    return render(request, 'Familia/About.html')