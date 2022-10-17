from django import forms

class MiFamilia(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    
class Buscador(forms.Form):
    nombre= forms.CharField(max_length=30, required=False)