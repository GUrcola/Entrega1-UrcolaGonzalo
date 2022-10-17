from contextlib import redirect_stderr
from re import template
from django.http import HttpResponse
from django.template import Context, Template
# loader
from Familia.models import familiares
from django.shortcuts import render, redirect
from Familia.forms import MiFamilia, Buscador

def crear_familiar (request):
    if request.method =='POST':
        formulario= MiFamilia(request.POST)
        if formulario.is_valid(): 
            data=formulario.cleaned_data
            nombre= data ['nombre']
            apellido= data ['apellido']
            edad= data ['edad']
            familia= familiares(nombre=nombre,apellido=apellido)
            familia.save()
            return redirect('ver_familia')    
    
    
    formulario= MiFamilia()
        
    # template= loader.get_template('crear_familiar.html')
    # template_renderizado= template.render()
    # return HttpResponse (template_renderizado)  
    return render(request,'Familia/crear_familiar.html',{'formulario':formulario})



def ver_familia (request):
    
   nombre= request.GET.get('nombre', None)
   
   if nombre:
       familia= familiares.objects.filter(nombre_icontains= nombre) 
   else:
       familia= familiares.objects.all()    
  
     
   formulario= Buscador()
   
   return render(request,'Familia/ver_familia.html',{'familia':familia, 'formulario': formulario}) 

def index (request):
    return render(request, 'Familia/index.html')

def About (request):
    return render(request, 'Familia/About.html')