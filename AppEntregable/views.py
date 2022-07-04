from django.http import HttpResponse
from django.shortcuts import render
from AppEntregable.models import Papa

# Create your views here.
def papa(self):
    papa=Papa(nombre="Yldemar", apellido="Gutierrez", edad=60)
    papa.save()
    texto=f"familiar creado: {papa.nombre} {papa.apellido} {papa.edad}"
    return HttpResponse(texto)
    