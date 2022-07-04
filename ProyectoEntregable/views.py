from django.http import HttpResponse
from django.template import Context, Template, loader

def ProyectoEntregable1(self):

    fami1= "Yldemar"
    fami2= "Rosilinda"
    fami3= "Xavier"

    diccionario={'familiar1':fami1,'familiar2':fami2,'familiar3':fami3}
    plantilla2=loader.get_template('template2.html')
    documento=plantilla2.render(diccionario)
    return HttpResponse(documento)

